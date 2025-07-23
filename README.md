# 环境安装

我们的代码主要基于 [Newclid](https://github.com/LMCRC/Newclid) 构建，也主要需要按照这个包。其余的包遇到报错直接 pip install 就可以了。

安装 Newclid 不能直接 pip install，需要从 github 源码安装，在终端执行下面的指令就可以了：

```bash
pip install git+https://github.com/LMCRC/Newclid.git
```

安装完成后，在脚本中可以执行 `import Newclid` 就安装成功了。

# 代码介绍

首先可以熟悉一下构造数据流程，也就是从 `./build_problem.py` 这个文件开始。之前已经说过，构造一个问题和 proof 由三个部分组成，分别是 clauses(或者叫 definition)，statement，和 rules。
一个问题由多个 clauses 组成，每个 clause 可以对应生成多个初始 statement（初始的 statement 可以视为前提条件 premises）。
因此一个题目被描述出来的时候，就自然形成了对应的前提条件。在 `./build_problem.py` 这个文件的第 180 行就是一个问题描述的例子。
它包含 5 个 clauses，每个 clauses 之间通过 `;` 隔开。值得注意的是，这里只写了问题的描述 （caption），并没有写具体要求解的问题。
这也是我们数据引擎构造数据的方法。就是首先通过 DDAR 把这个 caption 中所有能推导出来的 statement 全部推导出来。然后这些 statement 中随机一个 statement 都可以作为最终要求解的问题。

在终端中运行 `python build_problem.py` 就可以得到 `./outputs/test_solution.json` 和 `./outputs/test_image.png` 这两个文件。
前者就是根据这个 caption 得到的所有 statement 的求解过程。后者则是这个 caption 对应的图像。这里也可以看到，即使最终的问题不一致，只要 caption 一样，图像都是一样的。
一个标准的问题应该类似 `a = free a; b = lconst b a 18; c = on_dia c a b; d = on_dia d a c; e f g h = cc_tangent e f g h b c d a ? eqangle e g e h f g f h `。
`?` 前是 caption，`?` 后是要求解的 statement。具体每个 clause 是什么意思大家可以参考 [官方文档](https://lmcrc.github.io/Newclid/manual/default_files/definitions.html)

`./build_problem.py` 这个代码大家可以详细看一下，有什么问题下次答疑的时候都可以提出来。然后我们进入正题，辅助线数据的构建。
一共是两种辅助线的构建方法，一个是 alphageometry 提出的反向构建方法，在 `./aux_point_alphageo.py` 中，另一个是正向构建的方法 `./aux_point.py`。

运行 `python aux_point_alphageo.py` 可以得到 `./outputs/aux_alphageo.json` 的结果。（运行比较久）

运行 `python aux_point.py` 可能可以得到 `./outputs/aux.json` 的结果。（运行比较久，而且由于采样的随机性，所以可能得不到结果）。这个也是我们需要人工构建基础场景的原因。

# 任务

首先还是搭建环境，尝试理解这些代码。有问题的话可以记录下来，下次答疑的时候，我们可以一起讨论。代码缺少注释，可以让 LLM 帮助解释。

然后尝试为 `./aux_point.py` 写一些基础 caption，最好把对应的辅助线也写上。这个任务大家可以先构思一下想法，不一定要立刻做，下次答疑我们交流一下，然后定一下数据格式。