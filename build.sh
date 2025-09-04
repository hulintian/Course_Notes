input="$1"
output="$1"

pandoc "$input".md -o ($output).pdf \
  --pdf-engine=xelatex \
  -V mainfont="Noto Serif" \
  -V CJKmainfont="Noto Serif CJK SC" \
  -V monofont="JetBrains Mono" \
  -V geometry:margin=25mm
