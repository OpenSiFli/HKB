# `docs.sifl.com/projects`文档模板

## 安装工具链
1. 安装 Python 3.x，并确保在命令行中执行`python --version`能显示python版本
1. 在命令行中执行 `pip install -r requirements.txt`，安装编译文档所需的工具包`sifli-docs-toolbox`

## 生成文档
在文档根目录的命令行下执行下面的命令即可生成文档，
```shell
sf-build-docs --lang zh_CN --version latest
```

`--lang`配置生成文档的语言，`zh_CN`为中文，`en`为英文，缺省为中文。`--version`配置版本号, 不配置则为`latest`。CI编译时会自动获取标签作为版本号

双击`build/zh_CN/html/index.html`可以打开生成的中文文档。

点击[链接](https://docs.sifli.com/projects/doc-template/latest/zh_CN/index.html)浏览网站效果


## 定制
### 项目名称
项目配置文件位于`source/en/conf.py`和`source/zh_CN/conf.py`，分别对应英文版和中文版

把`conf.py`里的`project`变量值由`foo`改为实际项目的名字即可修改项目名称

### 部署的网站路径
文件`.github\workflows\build-docs.yml`为github的`Actions`配置文件，修改其中`PROJ_NAME`环境变量即可修改文档的部署地址，如把`PROJ_NAME`由`doc-template`改为`test-doc`，部署的文档网址就是`docs.sifli.com/projects/test-doc`，包含版本号和语言的网址则是
`docs.sifli.com/projects/test-doc/latest/en`和`docs.sifli.com/projects/test-doc/latest/zh_CN`，`latest`为版本号，`en`和`zh_CN`为语言。

配置文件中屏蔽了push事件触发的文档构建流水线，放开如下的被注释掉的`push:`代码段就可以启用push事件，每次提交代码都会触发文档构建。

```yaml
on:
  # Uncomment the following lines to enable automatic triggering on push events
  # push:
  #   branches:
  #     - main
  #     - 'release/*'
  #   paths:
  #     - 'source/**'
  #   tags:
  #     - '*'
  workflow_dispatch:  # 允许手动触发

```



提交后会自动触发文档的编译，没有标签的节点会以`latest`版本编译，有标签的节点则以标签名称为版本号编译。

### 版本号
根目录下的`version.json`为版本号列表，在其中添加需要在版本下拉框中显示的版本号，同时还支持分支版本，由`"type": "branch"`指定，类似主分支的latest版本，他表示某个分支的最新版本。

如果不需要版本选择框，可以修改`conf.py`，将`html_context`字典中的`versions`删除，如下
```py
del html_context['versions']
```

### 多语言
如果不需要配置选择语言，可以修改`conf.py`，将`html_context`字典中的`languages`删除，如下

```py
del html_context['languages']
```

### 其他配置
`sifli_docs_toolbox`的`docs_conf.py`文件中定义了一些`conf.py`所需的公共配置，通过`from sifli_docs_toolbox.docs_conf import *` 引入了`conf.py`，如需修改默认配置，可以在`conf.py`中修改相应的python变量，类似上文中修改`html_context`变量。
