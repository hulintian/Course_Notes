import os
import re
import pandas as pd
from datetime import datetime
from pyecharts.charts import Bar, Timeline
from pyecharts import options as opts

# === 配置 ===
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
OUTPUT_HTML = os.path.join(os.path.dirname(__file__), "earthquake_monthly_bar_race.html")

TOP_K = 10
USE_COUNT = True   # True=次数, False=最大震级

# 中英文映射表
REGION_MAP = {
    "sichuan": "四川",
    "xinjiang": "新疆",
    "xizang": "西藏",
}

DATE_COL_CANDIDATES = ["发震日期（北京时间）", "发震时间", "时间", "日期", "发生时间"]
MAG_COL_CANDIDATES  = ["震级(M)", "震级", "M", "Magnitude"]

def find_col(cols, candidates):
    for c in candidates:
        if c in cols:
            return c
    return None

def load_one_xlsx(path):
    name = os.path.basename(path)
    region = re.sub(r"\.xlsx$", "", name, flags=re.I)
    region = re.sub(r"_?earthquake", "", region, flags=re.I)
    region = REGION_MAP.get(region.lower(), region)  # 映射成中文

    df = pd.read_excel(path, engine="openpyxl")

    date_col = find_col(df.columns, DATE_COL_CANDIDATES)
    mag_col = find_col(df.columns, MAG_COL_CANDIDATES)

    df = df.rename(columns={date_col: "datetime"})
    if mag_col:
        df = df.rename(columns={mag_col: "magnitude"})
    else:
        df["magnitude"] = None

    df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")
    df["month"] = df["datetime"].dt.to_period("M").astype(str)
    df["region"] = region
    return df[["month", "region", "magnitude"]]

def load_all_xlsx(data_dir):
    files = [os.path.join(data_dir, f) for f in os.listdir(data_dir)
             if f.lower().endswith(".xlsx")]
    dfs = []
    for f in files:
        try:
            dfs.append(load_one_xlsx(f))
        except Exception as e:
            print(f"[WARN] 读取失败: {f} -> {e}")
    return pd.concat(dfs, ignore_index=True)

def build_monthly_stats(df):
    cnt = df.groupby(["month", "region"]).size().reset_index(name="count")
    maxmag = (
        df.dropna(subset=["magnitude"])
          .groupby(["month", "region"])["magnitude"]
          .max()
          .reset_index(name="max_magnitude")
    )
    return cnt, maxmag

def main():
    df_all = load_all_xlsx(DATA_DIR)
    cnt_df, maxmag_df = build_monthly_stats(df_all)

    metric_df = cnt_df.rename(columns={"count": "value"}) if USE_COUNT \
                else maxmag_df.rename(columns={"max_magnitude": "value"})
    metric_name = "地震次数" if USE_COUNT else "最大震级"
    all_months = sorted(metric_df["month"].unique())

    timeline = Timeline(init_opts=opts.InitOpts(width="1000px", height="600px"))
    timeline.add_schema(play_interval=1200, is_auto_play=True, is_loop_play=True)

    for m in all_months:
        month_df = metric_df[metric_df["month"] == m].copy()
        # 按数值排序，取 Top K
        month_df = month_df.sort_values("value", ascending=True).tail(TOP_K)

        bar = (
            Bar()
            .add_xaxis(list(month_df["region"]))
            .add_yaxis(metric_name, list(month_df["value"]))
            .reversal_axis()
            .set_global_opts(
                title_opts=opts.TitleOpts(title=f"{m} 各省份{metric_name}排行榜"),
                xaxis_opts=opts.AxisOpts(name=metric_name),
                yaxis_opts=opts.AxisOpts(name="省份"),
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="right"))
        )
        timeline.add(bar, time_point=str(m))

    timeline.render(OUTPUT_HTML)
    print(f"[OK] 排行榜动画生成 → {OUTPUT_HTML}")

if __name__ == "__main__":
    main()
