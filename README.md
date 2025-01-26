# csdn-exporter

## 介绍

CSDN 文章导出，支持 Markdown, PDF 格式

功能：

1. 支持单篇文章导出
2. 支持专栏文章批量导出
3. 支持将导出的多篇文章合并为一篇，以便全局搜索
4. 文章中的图片可下载到本地，或使用外链形式

## 使用

### 修改配置

1、获取某作者的全部文章

eg: https://blog.csdn.net/blogdevteam/

修改 run.bat

```bat
download_category = True
download_article = False
set user_name=blogdevteam
```

### 运行脚本

- Windows 运行 `run.bat`（双击打开或者在终端中运行）
- macOS / Linux 运行 `./run.sh`

2、获取某篇文章

修改 run.bat

```bat
download_category = False
download_article = True
set article_url="https://blogdev.blog.csdn.net/article/details/119778725"
```

本仓库改进于 https://github.com/allenmirac/CSDNExporter