# 贡献者指南 / Contributing Guide

> 本指南专为不熟悉 GitHub 操作的队友编写。  
> 全程只需要用浏览器操作，**不需要安装任何软件或输入任何命令**。  
> 有任何问题请联系 Louis 或小志。
>
> 本项目通过 GitHub 进行协作。仓库用于存放所有重要的**过程产出文件**（如剧本、分镜图、提示词、工作流等），以及团队协作所需的文档。
>
> **请勿上传大型文件**，例如 AI 模型、视频文件等。此类文件体积庞大，不适合存放在代码仓库中。最终的视频产出由 Louis 统一整理，放置在 README 文档中呈现。

---

## 目录

1. [准备工作](#1-准备工作)
2. [文件夹结构说明](#2-文件夹结构说明)
3. [详细步骤](#3-详细步骤)
4. [文件命名规范](#4-文件命名规范)
5. [常见问题](#5-常见问题)

---

## 1. 准备工作

### 1.1 注册 GitHub 账号

1. 打开 https://github.com
2. 点击 **Sign up**（注册）
3. 输入邮箱、密码、用户名（选择一个简单的用户名，建议用拼音）
4. 完成验证
5. 注册完成后**告诉 Louis 你的 GitHub 用户名**

### 1.2 Fork 这个仓库

Fork 的意思是：把项目复制一份到你自己的 GitHub 账号下。

1. 打开浏览器，访问：https://github.com/liusenjun/human-brake-ai-video
2. 点击右上角 **Fork** 按钮
3. 等待几秒，页面跳转到**你账号下**的仓库
4. 现在 URL 应该类似：`https://github.com/你的用户名/human-brake-ai-video`
5. ✅ 完成！以后所有修改都在这个仓库里进行

> **提示**：Fork 只需要做一次。之后每次贡献都从你账号下的这个 Fork 开始。

---

## 2. 文件夹结构说明

### 整个项目的文件夹是这样的：

```
human-brake-ai-video/
├── louis/              ← Louis · Act 1
├── huangyishu/        ← 黄奕舒 · Act 2-3
├── jing/               ← 辛怡静 · Act 2-3
├── leozhu/             ← 朱智立 · Act 4
│
├── script/             ← 原始剧本（共用）
├── workflows/          ← 技术工作流（共用）
├── audio/              ← 配乐（共用）
└── voice/              ← 配音（共用）
```

### 放文件的规则：

| 如果你的文件是…… | 就放到…… |
|-----------------|---------|
| 剧本、原始脚本 | `script/` |
| ComfyUI 工作流、Python 脚本 | `workflows/` |
| 配乐文件或链接 | `audio/` |
| 配音文件或链接 | `voice/` |
| **你负责的 Act 的分镜图、提示词等** | **你自己的文件夹**（`louis/`、`huangyishu/` 等） |

### 每个人负责什么：

| 成员 | 文件夹 | 负责内容 |
|------|--------|---------|
| Louis | `louis/` | Act 1：文戏分镜、提示词、工作流 |
| 黄奕舒 | `huangyishu/` | Act 2-3：追逐场景分镜、视觉效果 |
| 辛怡静 | `jing/` | Act 2-3：追逐场景分镜、视觉效果 |
| 朱智立 | `leozhu/` | Act 4：追逐尾声分镜、视觉效果 |

> **提示**：每个人文件夹内部的结构**不需要完全一致**——你有什么就放什么，没有的类别可以空着。

---

## 3. 详细步骤

### Step 1：打开你的仓库

1. 打开浏览器，进入你的 Fork 仓库：
   `https://github.com/你的用户名/human-brake-ai-video`

---

### Step 2：进入你的文件夹

1. 在仓库页面，找到并点击**你的文件夹**（例如 `huangyishu/`）
2. 确认 URL 变成了类似：
   `https://github.com/你的用户名/human-brake-ai-video/tree/main/huangyishu`
3. ✅ 现在你已经在你的文件夹里面了

---

### Step 3：添加文件

**方式 1：上传已有文件（推荐）**

1. 点击绿色的 **"Add file"** 按钮
2. 选择 **"Upload files"**
3. 把你的文件拖进去，或点击 "choose your files" 选择文件
4. **此时注意：你已经在你的文件夹里了，文件会自动落入这个文件夹**
5. 页面底部写提交说明，例如：`Add Act 2 storyboard images`
6. 点击绿色的 **"Commit changes"** 按钮

**方式 2：在网页上直接创建新内容**

1. 点击绿色的 **"Add file"** 按钮
2. 选择 **"Create new file"**
3. 在顶部文件名框输入文件名（例如 `shot01_prompt.md`）
4. 在下方大文本框粘贴或输入内容
5. **此时注意：文件会落入你当前所在的文件夹**
6. 底部写提交说明，点击 **"Commit changes"** 按钮

---

### Step 4：发起 Pull Request（申请合并）

当你完成文件添加后，需要申请把你的修改合并到原始仓库。

1. 在你的仓库页面，你会看到一个黄色的提示条：
   > **"你的仓库有比主仓库多的提交"**
   > **[Compare & pull request]** 按钮
2. 点击 **"Compare & pull request"**
3. 检查以下是否正确：
   - `base repository` → `liusenjun/human-brake-ai-video`
   - `base` → `main`
   - `head repository` → `你的用户名/human-brake-ai-video`
   - `compare` → `main`
4. 标题写清楚这次贡献的内容，例如：`Add Act 2 storyboard images`
5. 可以留言说明
6. 点击绿色的 **"Create pull request"** 按钮
7. ✅ 完成！Louis 会收到通知并审核

---

### 如果要添加到公共文件夹（workflows/、audio/ 等）

1. 先点击仓库顶部的 **"human-brake-ai-video"** 回到根目录
2. 点击进入对应的公共文件夹（例如 `workflows/`）
3. URL 应该变成：`https://github.com/你的用户名/human-brake-ai-video/tree/main/workflows`
4. 再执行 **Step 3** 的操作

---

### 之后每次贡献（重复 Step 2-4）

1. 打开你的仓库
2. 进入你的文件夹
3. 添加或修改文件
4. Commit changes
5. 点 **"Compare & pull request"** → **"Create pull request"**

---

## 4. 文件命名规范

> 文件上传后如果发现文件名有问题，再按规范修改即可。不需要在上传前逐个检查。

**重命名方法：**
找到要改的文件，点文件名旁边的 **"..."** 菜单 → **"Rename"** → 输入新文件名 → 点 **"Commit changes"**。

**规范如下：**

- ✅ **使用英文、拼音或数字**
- ✅ **单词之间用下划线 `_` 或连字符 `-` 分隔**
- ✅ **全部用小写**
- ❌ **不要用空格**
- ❌ **不要用特殊字符**

| 文件类型 | 命名示例 |
|---------|---------|
| 分镜图 | `shot01.png`, `act2_shot03.png` |
| 提示词文档 | `shot01_prompt.md`, `act1_prompts.docx` |
| 剧本 | `act1_script_v1.docx` |
| 角色设定 | `character_robin.md` |

---

## 5. 常见问题

### Q1：提交后发现写错了，怎么修改？

在 GitHub 页面上找到那个文件，点击文件名进入文件内容页面，点右上角**铅笔图标 ✏️** 即可重新编辑，编辑完成后点 **"Commit changes"**。

---

### Q2：想删除一个文件怎么办？

在 GitHub 页面上找到那个文件，点击文件名进入文件内容页面，点右上角**垃圾桶图标**即可删除，然后点 **"Commit changes"**。

---

### Q3：提交 PR 后发现有问题，能撤回吗？

可以！在你的 Pull Request 页面，点右上角 **"Close"** 按钮即可关闭，不会影响原始仓库。

---

### Q4：Sync fork 是什么？什么时候需要点？

如果 Louis 在原始仓库做了更新，你会看到黄色的提示条写着 **"This branch is out of date"**，这时需要：

1. 点 **"Sync fork"** 按钮
2. 点 **"Update branch"**
3. 等待更新完成，再继续添加你的文件

---

## 需要帮助？

如果遇到本指南没有覆盖的问题，请联系 **Louis** 或通过 Discord 联系 **小志**（AI 技术搭档）。

---

*本指南由小志（OpenClaw AI Agent）编写，2026*
