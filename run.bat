@echo off
@title CSDNExporter

@REM 是否批量下载文章
set download_category="true"
@REM CSDN 用户 ID（非昵称）
set user_name=your_username
set start_page=1
set page_num=300

@REM 是否单独下载文章
set download_article="false"
set article_url=""

@REM 保存目录
set markdown_dir=markdown
set pdf_dir=pdf

@REM 生成全部专栏链接
if %download_category% == "true" (
  echo "Get blog directory link: Save in category_links_username.txt..."
  python -u link.py %user_name%
)

for /f "tokens=* delims=" %%a in (category_links_%user_name%.txt) do (
    @REM echo %%a
    if %download_category% == "true" (
      echo "Batch download"
      python -u main.py ^
          --category_url %%a ^
          --start_page %start_page% ^
          --page_num %page_num% ^
          --markdown_dir %markdown_dir% ^
          --pdf_dir %pdf_dir% ^
          --combine_together ^
          --is_win 1
          @REM --to_pdf ^
          @REM --with_title ^
          @REM --rm_cache
    )
)

if %download_article% == "true" (
  echo "Download an article"
  python -u main.py ^
      --article_url %article_url% ^
      --markdown_dir %markdown_dir% ^
      --with_title ^
      --rm_cache ^
      --is_win 1
)

pause