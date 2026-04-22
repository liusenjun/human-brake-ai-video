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

Clone 的意思是：把你在 GitHub 上的仓库下载到你自己电脑上，以后就可以在电脑里编辑文件了。

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

> **提示**：克隆地址里的 `.git` 不要漏掉，这是 Git 仓库的标识。  
> **提示**：如果你用的是中文版 Windows，可能需要在命令提示符里先切换到合适的目录。比如你想把仓库放在 D:\projects\ 下，就先输入 `cd D:\projects`，再执行 clone 命令。

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
3. 按回车，如果看到类似 `(你的名字)` 出现在命令提示符前面，说明创建成功
   - 例如：`C:\Projects\human-brake-ai-video (wangxiaoming)>`

> **提示**：分支名建议用**英文或拼音**，不要用中文，否则可能出现编码问题。  
> **提示**：每次开始新工作时，先确认你在自己的分支上（命令提示符前有你的分支名）。

---

### Step 4：添加或修改文件

现在你可以往仓库里添加你的文件了。

**操作步骤：**

1. 打开文件资源管理器，进入 `human-brake-ai-video` 文件夹
2. 根据你的贡献类型，找到对应的文件夹（参考下一节"文件夹说明"）
3. 把你的文件粘贴进去，或者修改已有的文件

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
   - Git 会显示所有你修改过的文件（显示为红色或绿色）
3. 把你要提交的文件加入暂存区（把红色变成绿色）：
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
   - 提交说明要写清楚你做了什么
   - 示例：`git commit -m "添加角色设定文档"`
   - 示例：`git commit -m "修改 shot03 背景描述"`

> **提示**：每次 Commit 最好只做一件事，这样有问题时容易回溯。  
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
   - 按提示输入你的 GitHub 用户名和密码
   - 注意：密码输入时屏幕不会显示任何字符，这是正常的，输入完直接回车即可
3. 推送成功后，刷新你的 GitHub 仓库页面，会看到你的分支已经出现了

> **提示**：如果你用的是 GitHub 账号密码登录，最近 GitHub 可能要求使用 **Personal Access Token** 代替密码。  
> 创建 Token 的方法：在 GitHub 页面右上角点你的头像 → Settings → Developer settings → Personal access tokens → Generate new token → 勾选 `repo` → 生成。把生成的 Token 复制下来，当作密码使用。  
> 如果遇到登录问题，请联系 Louis 或小志协助。

---

### Step 7：发起 Pull Request

Pull Request（PR）的意思是：申请把你分支里的修改，合并到原始仓库（liusenjun/human-brake-ai-video）里去。

**操作步骤：**

1. 打开你的 GitHub 仓库页面
2. 你会看到一个黄色的提示条：**"你的分支名 had recent pushes"**，旁边有个 **"Compare & pull request"** 按钮
3. 点击 **"Compare & pull request"**
4. 在 PR 页面，填写以下信息：
   - **Title（标题）**：写清楚这次贡献的内容
     - 例如：`添加角色设定文档` 或 `更新 shot05 的提示词`
   - **Leave a comment（留言）**：可以写一些说明，比如你做了什么、有什么需要队友注意的
5. 检查一下：
   - `base repository` 应该是 `liusenjun/human-brake-ai-video`
   - `base` 应该是 `main`
   - `head repository` 应该是 `你的用户名/human-brake-ai-video`
   - `compare` 应该是 `你的分支名`
6. 确认无误后，点击绿色的 **"Create pull request"** 按钮
7. 创建成功后，Louis 会在 GitHub 上收到通知，并审核你的 PR

> **提示**：提交 PR 后，你可以在 GitHub 仓库的 "Pull requests" 页面看到你的申请状态。  
> **提示**：如果 Louis 需要你修改什么，GitHub 会通知你，你只需要在电脑上继续修改、commit、push，PR 会自动更新。

---

## 5. 文件夹说明：你的文件应该放在哪里？

根据你负责的内容，把文件放到对应文件夹：

| 你负责的内容 | 放到哪个文件夹 | 说明 |
|-------------|---------------|------|
| 剧本、故事大纲 | `script/` | docx、txt、md 格式 |
| 分镜图、故事板图片 | `storyboard/images/` | png、jpg 格式 |
| 视频生成提示词 | `prompts/` | docx、md 格式 |
| ComfyUI 工作流 | `workflows/` | json 格式 |
| 视频文件（不传大文件） | `videos/` | 只放链接，参考 videos/README.md |
| 角色设定、角色描述 | `credits/` | md、txt 格式 |
| 配乐、音效 | `credits/audio/` | mp3、wav 链接或说明 |
| 配音、台词录音 | `credits/voice/` | mp3 链接或说明 |
| 其他创作内容 | `credits/你的名字/` | 按贡献者名字建子文件夹 |

### credits/ 目录结构示例

```
credits/
├── README.md              ← 贡献者总览
├── audio/                ← 配乐
│   └── [待添加]
├── voice/                ← 配音
│   └── [待添加]
├── [队友A]/              ← 队友A的贡献
│   └── [队友A的文件]
└── [队友B]/              ← 队友B的贡献
    └── [队友B的文件]
```

---

## 6. 文件命名规范

为了保持仓库整洁，所有文件名请遵循以下规则：

### 基本规则

- ✅ **使用英文、拼音或数字**（不要用纯中文文件名）
- ✅ **单词之间用下划线 `_` 或连字符 `-` 分隔**
- ✅ **全部用小写**（统一风格）
- ❌ **不要用空格**
- ❌ **不要用特殊字符**（如 `!@#$%^&*()` 等）

### 命名格式建议

| 文件类型 | 命名示例 |
|---------|---------|
| 分镜图 | `shot01.png`, `shot02_scene.png` |
| 提示词文档 | `shot01_kling_prompt.md`, `act1_prompts.docx` |
| 角色设定 | `character_robin_v1.md`, `角色名_description.md` |
| 配乐说明 | `bgm_track01.md`, `scene2_music.txt` |
| 配音脚本 | `voice_shot01.md`, `robin_lines.md` |

---

## 7. 常见问题与解决方法

### Q1：git clone 时显示 "Could not resolve host"

**原因**：电脑没有连接网络，或者 DNS 设置有问题。  
**解决方法**：
1. 打开浏览器确认能否访问 github.com
2. 如果不能，重启路由器
3. 如果能，尝试换一个网络（有些公司/学校网络会屏蔽 GitHub）

---

### Q2：git push 时要求输入用户名和密码，然后显示 "Authentication failed"

**原因**：GitHub 2021 年后不再支持密码登录，需要使用 Personal Access Token。  
**解决方法**：
1. 登录 GitHub，点击右上角头像 → **Settings**
2. 左侧菜单找到 **Developer settings**
3. 点击 **Personal access tokens** → **Generate new token**
4. 在 "Select scopes" 里勾选 **repo**（完全控制）
5. 点击 **Generate token**，复制显示的 Token（这是一串很长的字符）
6. 以后 git push 时，用户名输入 GitHub 用户名，密码输入这个 Token（不是你的 GitHub 密码）

---

### Q3：git add 时显示 "warning: LF will be replaced by CRLF"

**原因**：Windows 换行符和 Unix 换行符不同，Git 自动做了转换，这是正常的，不是错误，可以忽略。

---

### Q4：Commit 时显示 "nothing to commit, working tree clean"

**原因**：你没有做任何修改，或者文件路径不对。  
**解决方法**：
1. 输入 `git status` 查看文件状态
2. 确认你的文件确实放进了仓库的文件夹里
3. 如果文件很大（比如视频），确认没有超出 GitHub 的文件大小限制（单文件超过 100MB 需要用 Git LFS）

---

### Q5：Push 时显示 "rejected"

**原因**：你的分支落后于远程仓库（别人在你克隆之后提交了新内容）。  
**解决方法**：
1. 先拉取最新内容：`git pull origin main`
2. 如果有冲突，手动解决冲突（通常是你的修改和别人的修改在同一行）
3. 解决后重新 add、commit、push
4. 如果不熟悉解决冲突，联系 Louis 或小志协助

---

### Q6：Pull Request 提交后发现有问题，可以撤回吗？

**可以！** 在 GitHub 的 Pull Request 页面，可以随时关闭（Close）或者修改（Edit）你的 PR。关闭后重新发起新的即可，不会影响原始仓库。

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
| Conflict | 冲突 | 两个人同时改了同一行代码 |
| Remote | 远程 | GitHub 上的仓库（相对于本地） |
| Origin | 源 | 默认的远程仓库别名 |
| Main / Master | 主分支 | 仓库的主要版本所在分支 |

---

## 需要帮助？

如果遇到本指南没有覆盖的问题，请：

1. 联系 **Louis**（项目主导）
2. 联系 **小志**（AI 技术搭档，小志是 OpenClaw AI Agent，可以通过 Discord 与 Louis 沟通协助）

---

*本指南由小志（OpenClaw AI Agent）编写，2026*
