# 贡献者指南 / Contributing Guide

> 本指南专为不熟悉 GitHub 操作的队友编写。  
> 每一步都有详细说明，照着做即可。有任何问题请联系 Louis 或小志。

---

## 目录 / Table of Contents

1. [什么是 GitHub？](#1-什么是-github)
2. [准备工作：安装 Git 与登录 GitHub](#2-准备工作安装-git-与-登录-github)
3. [贡献流程概述](#3-贡献流程概述)
4. [详细步骤](#4-详细步骤)
   - [Step 1：在 GitHub 上 Fork 项目](#step-1在-github-上-fork-项目)
   - [Step 2：将 Fork 后的项目克隆到本地](#step-2将-fork-后的项目克隆到本地)
   - [Step 3：创建自己的分支](#step-3创建自己的分支)
   - [Step 4：添加或修改文件](#step-4添加或修改文件)
   - [Step 5：提交更改（Commit）](#step-5提交更改commit)
   - [Step 6：推送更改到你的 GitHub](#step-6推送更改到你的-github)
   - [Step 7：发起 Pull Request](#step-7发起-pull-request)
5. [文件夹说明：你的文件应该放在哪里？](#5-文件夹说明你的文件应该放在哪里)
6. [文件命名规范](#6-文件命名规范)
7. [常见问题与解决方法](#7-常见问题与解决方法)
8. [词汇表](#8-词汇表)

---

## 1. 什么是 GitHub？

**GitHub** 是一个用于存放代码和文件的平台，最大的特点是：**多人可以同时编辑同一个项目，而不会互相覆盖对方的修改**。

可以把 GitHub 想象成一个**共享文件夹**，但比普通共享文件夹多了一个"历史记录"功能——每一次谁改了什么、什么时候改的，都能清清楚楚看到。

### 几个核心概念

| 概念 | 通俗解释 |
|------|----------|
| **Repository（仓库）** | 一个项目文件夹，包含所有文件和历史记录 |
| **Fork（叉）** | 把别人的仓库复制一份到自己账号下，作为你修改的起点 |
| **Clone（克隆）** | 把 GitHub 上的仓库下载到你自己电脑上 |
| **Commit（提交）** | 保存一次修改，附带说明这次改了什么 |
| **Push（推送）** | 把电脑上的修改上传到 GitHub |
| **Pull Request（拉取请求）** | 申请把你的修改合并到原始仓库 |

---

## 2. 准备工作：安装 Git 与登录 GitHub

### 2.1 检查你是否已安装 Git

打开**命令提示符**（Win+R，输入 `cmd`，回车），输入：

```
git --version
```

如果显示类似 `git version 2.x.x` 的字样，说明已经安装，可以跳过 2.2。

如果显示"'git' 不是内部或外部命令"，请继续下一步安装。

### 2.2 安装 Git（Windows）

1. 打开 https://git-scm.com/download/win
2. 下载对应你电脑版本的安装程序（64-bit 或 32-bit）
3. 运行安装程序，全程点 **Next** 即可，**不需要改任何设置**
4. 安装完成后，重新打开命令提示符，输入 `git --version` 确认安装成功

### 2.3 登录 GitHub

1. 打开 https://github.com
2. 点击右上角 **Sign in**，输入你的账号密码登录
3. 如果没有账号，点击 **Sign up** 免费注册

> 注意：这一步需要你自己完成 GitHub 账号注册。小志无法替你注册。注册后告诉 Louis 你的 GitHub 用户名。

---

## 3. 贡献流程概述

```
[原始仓库]  →  Fork（复制到你的账号）
     ↓
  Clone（下载到电脑）
     ↓
  创建分支（你的工作区）
     ↓
  添加/修改文件
     ↓
  Commit（保存修改）
     ↓
  Push（上传到 GitHub）
     ↓
  Pull Request（申请合并到原始仓库）
     ↓
  [Louis 审核] → 合并（Merge）
```

整个流程只需要做一次准备工作（第 1-3 步），之后每次贡献只需要做第 4-7 步。

---

## 4. 详细步骤

### Step 1：在 GitHub 上 Fork 项目

Fork 的意思是：把 `liusenjun/human-brake-ai-video` 这个仓库，完整复制一份到你的 GitHub 账号下。

**操作步骤：**

1. 打开浏览器，访问：https://github.com/liusenjun/human-brake-ai-video
2. 在页面右上方，找到并点击 **Fork** 按钮（图标像一个叉子 🔱）
3. 等待几秒，页面会跳转到 **你账号下** 的新仓库
   - 新仓库的地址会变成：`https://github.com/你的用户名/human-brake-ai-video`
4. 这就是你的 Fork，以后所有修改都在这个仓库里进行

> **提示**：Fork 只需要做一次。之后每次贡献都从你账号下的这个 Fork 开始。

---

### Step 2：将 Fork 后的项目克隆到本地

Clone 的意思是：把你在 GitHub 上的仓库下载到你自己电脑上。

**操作步骤：**

1. 在你账号下的仓库页面，点击绿色的 **Code** 按钮
2. 点击 **HTTPS**，复制显示的链接（看起来像：`https://github.com/你的用户名/human-brake-ai-video.git`）
3. 打开命令提示符（Win+R，输入 `cmd`，回车）
4. 输入以下命令，把仓库克隆到你的电脑：
   ```
   git clone https://github.com/你的用户名/human-brake-ai-video.git
   ```
   - 比如你的用户名是 `xiaoming`，就输入：
     `git clone https://github.com/xiaoming/human-brake-ai-video.git`
5. 按回车，等待下载完成
6. 下载完成后，你会看到命令提示符所在目录下多了一个 `human-brake-ai-video` 文件夹

> **提示**：克隆地址里的 `.git` 不要漏掉。  
> **提示**：如果你想把仓库放在特定目录（比如 D:\projects\），先输入 `cd D:\projects`，再执行 clone 命令。

---

### Step 3：创建自己的分支

分支（Branch）的意思是：在你的仓库里创建一条独立的"时间线"。你的修改在这条时间线上进行，不会影响主线（main）的内容。

**为什么需要分支？**  
因为你和队友可能同时修改不同的地方。分支让每个人的工作互不干扰。

**操作步骤：**

1. 打开命令提示符，进入仓库目录：
   ```
   cd human-brake-ai-video
   ```
2. 创建一个以你名字命名的分支（把 `你的名字` 换成你的真实名字或昵称，用英文或拼音，无空格）：
   ```
   git checkout -b 你的名字
   ```
   - 比如你叫王小明，就输入：
     `git checkout -b wangxiaoming`
3. 按回车，如果看到类似 `(wangxiaoming)` 出现在命令提示符前面，说明创建成功

> **提示**：分支名建议用**英文或拼音**，不要用中文。  
> **提示**：每次开始新工作时，先确认你在自己的分支上。

---

### Step 4：添加或修改文件

#### 先搞清楚文件夹结构

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

**放文件的规则：**

| 如果你的文件是…… | 就放到…… |
|-----------------|---------|
| 剧本、原始脚本 | `script/` |
| ComfyUI 工作流、Python 脚本 | `workflows/` |
| 配乐文件或链接 | `audio/` |
| 配音文件或链接 | `voice/` |
| **你负责的 Act 的分镜图、提示词等** | **你自己的文件夹**（`louis/`、`huangyishu/` 等） |

#### 然后操作

**第一步：进入正确的文件夹**

1. 在你的仓库页面，找到并点击你的文件夹（例如 `huangyishu/`）
2. 确认进入了文件夹里面，URL 应该类似：
   `https://github.com/你的用户名/human-brake-ai-video/tree/main/huangyishu`
3. **现在你在这个文件夹里面了，添加的文件会自动落入这里**

**第二步：添加文件**

1. 点击绿色的 **"Add file"** 按钮
2. 选择 **"Upload files"**（上传已有文件）或 **"Create new file"**（在网页上写新内容）
3. **注意：此时你已经在你的文件夹内了，添加的文件会自动落入这个文件夹**
4. 把文件拖进去，或粘贴内容
5. 底部写提交说明，例如：`Add Act 2 storyboard images`
6. 点击 **"Commit changes"**

**如果是添加到公共文件夹（workflows/、audio/ 等）：**

1. 先点击顶部的仓库名称回到根目录
2. 点击进入对应的公共文件夹（如 `workflows/`）
3. 再点 **"Add file"** → 操作同上

> **重要**：不要修改根目录下的 README.md 和 CONTRIBUTING.md，除非是 Louis 明确要求的。

---

### Step 5：提交更改（Commit）

当你完成修改后，需要把修改记录下来。这个记录动作叫做 "Commit"。

**操作步骤：**

1. 打开命令提示符，确保你在仓库目录且在正确的分支上
2. 先查看当前状态：
   ```
   git status
   ```
3. 把你要提交的文件加入暂存区：
   ```
   git add .
   ```
   - 这个 `.` 表示添加所有修改的文件
   - 如果只想添加某个特定文件，可以输入：
     `git add 文件夹/文件名.后缀`
4. 提交这次修改：
   ```
   git commit -m "提交说明"
   ```
   - 示例：`git commit -m "Add Act 2 storyboard images"`
   - 示例：`git commit -m "Update shot05 prompt"`

> **提示**：每次 Commit 最好只做一件事。  
> **提示**：提交说明要用**英文或中文**，不要为空。

---

### Step 6：推送更改到你的 GitHub

Push 的意思是：把你在电脑上提交的修改，上传到你在 GitHub 上的仓库。

**操作步骤：**

1. 在命令提示符里输入（把 `你的分支名` 换成你当前分支的名字）：
   ```
   git push origin 你的分支名
   ```
   - 如果你的分支叫 `wangxiaoming`，就输入：
     `git push origin wangxiaoming`
2. 第一次推送时，Git 可能要求你登录 GitHub
   - 用户名输入你的 GitHub 用户名
   - 密码输入你的 GitHub 密码（注意：输入时屏幕不会显示字符，这是正常的）
3. 推送成功后，刷新你的 GitHub 仓库页面，会看到你的分支已经出现了

> **注意**：如果 GitHub 登录失败，可能是因为 GitHub 不再支持密码登录，需要使用 **Personal Access Token**。创建方法见常见问题 Q2。

---

### Step 7：发起 Pull Request

Pull Request（PR）的意思是：申请把你分支里的修改，合并到原始仓库（liusenjun/human-brake-ai-video）里去。

**操作步骤：**

1. 打开你的 GitHub 仓库页面
2. 你会看到一个黄色的提示条：**"你的分支名 had recent pushes"**，旁边有个 **"Compare & pull request"** 按钮
3. 点击 **"Compare & pull request"**
4. 填写以下信息：
   - **Title（标题）**：写清楚这次贡献的内容
     - 例如：`Add Act 2 storyboard images`
   - **Leave a comment（留言）**：可以写一些说明
5. 检查：
   - `base repository` → `liusenjun/human-brake-ai-video`
   - `base` → `main`
   - `head repository` → `你的用户名/human-brake-ai-video`
   - `compare` → `你的分支名`
6. 确认无误后，点击绿色的 **"Create pull request"** 按钮
7. 创建成功后，Louis 会收到通知并审核

> **提示**：提交 PR 后，可以随时在 GitHub 的 "Pull requests" 页面看到状态。如果需要修改，继续在电脑上修改、commit、push，PR 会自动更新。

---

## 5. 文件夹说明：你的文件应该放在哪里？

### 项目整体结构

```
human-brake-ai-video/
├── louis/              ← Louis · Act 1
├── huangyishu/        ← 黄奕舒 · Act 2-3
├── jing/               ← 辛怡静 · Act 2-3
├── leozhu/             ← 朱智立 · Act 4
├── script/             ← 原始剧本（共用）
├── workflows/          ← 技术工作流（共用）
├── audio/              ← 配乐（共用）
└── voice/              ← 配音（共用）
```

### 每个人负责什么

| 成员 | 文件夹 | 负责内容 |
|------|--------|---------|
| Louis | `louis/` | Act 1：文戏分镜、提示词、工作流 |
| 黄奕舒 | `huangyishu/` | Act 2-3：追逐场景分镜、视觉效果 |
| 辛怡静 | `jing/` | Act 2-3：追逐场景分镜、视觉效果 |
| 朱智立 | `leozhu/` | Act 4：追逐尾声分镜、视觉效果 |

### 文件夹内的组织方式

每个人文件夹内部的结构**不需要完全一致**——你有什么就建什么，没有的类别可以空着或省略。

**示例（louis 的文件夹）：**
```
louis/
├── script/         ← Act 1 剧本相关
├── storyboard/     ← Act 1 分镜图
├── prompts/       ← Act 1 视频生成提示词
└── workflows/     ← Act 1 相关工作流
```

**示例（huangyishu 的文件夹，可能是）：**
```
huangyishu/
├── storyboard/     ← Act 2-3 分镜图
└── prompts/       ← Act 2-3 视频提示词
```

**共用文件夹（所有人都会用到）：**

| 文件夹 | 存放内容 |
|--------|---------|
| `script/` | 陈秋芳老师的原始剧本，所有人共用参考 |
| `workflows/` | ComfyUI 技术工作流，所有人共用 |
| `audio/` | 配乐文件（放链接或说明文档） |
| `voice/` | 配音文件（放链接或说明文档） |


---

## 6. 文件命名规范

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

## 7. 常见问题与解决方法

### Q1：git clone 时显示 "Could not resolve host"

**原因**：网络连接问题。  
**解决方法**：检查网络，重启路由器，或换一个网络环境。

---

### Q2：git push 时显示 "Authentication failed"

**原因**：GitHub 2021 年后不再支持密码登录，需要使用 Personal Access Token。  
**解决方法**：
1. GitHub 右上角头像 → **Settings**
2. 左侧 → **Developer settings** → **Personal access tokens**
3. **Generate new token** → 勾选 **repo** → **Generate**
4. 复制 Token（很长的一串字符）
5. 以后 git push 时，用户名输入 GitHub 用户名，**密码输入这个 Token**（不是你的 GitHub 密码）

---

### Q3：Commit 时显示 "nothing to commit, working tree clean"

**原因**：你没有做任何修改，或者文件没有放进正确的文件夹。  
**解决方法**：
1. 输入 `git status` 查看状态
2. 确认文件确实放进了仓库的对应文件夹里

---

### Q4：Push 时显示 "rejected"

**原因**：你的分支落后于远程仓库。  
**解决方法**：
1. 先拉取：`git pull origin main`
2. 如果有冲突，手动解决（或联系 Louis/小志协助）
3. 重新 add、commit、push

---

### Q5：Pull Request 提交后发现有问题，可以撤回吗？

**可以！** 在 GitHub 的 Pull Request 页面，可以随时关闭（Close）或修改（Edit），不会影响原始仓库。

---

## 8. 词汇表

| 英文 | 中文 | 解释 |
|------|------|------|
| Repository / Repo | 仓库 | 一个项目的所有文件加上历史记录 |
| Fork | 叉/复刻 | 把别人的仓库复制到自己账号下 |
| Clone | 克隆 | 把仓库从 GitHub 下载到本地电脑 |
| Branch | 分支 | 独立的修改时间线 |
| Commit | 提交 | 保存一次修改，带说明 |
| Push | 推送 | 把本地修改上传到 GitHub |
| Pull Request / PR | 拉取请求 | 申请把你的修改合并到原始仓库 |
| Merge | 合并 | 把你的修改正式并入主仓库 |
| Conflict | 冲突 | 两个人同时改了同一行内容 |
| Origin | 源 | 默认的远程仓库别名 |

---

## 需要帮助？

如果遇到本指南没有覆盖的问题，请联系 **Louis** 或通过 Discord 联系 **小志**（AI 技术搭档）。

---

*本指南由小志（OpenClaw AI Agent）编写，2026*
