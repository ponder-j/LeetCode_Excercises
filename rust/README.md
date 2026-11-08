# Rust Hot 100 本地刷题环境

对应原有的 `template.py`、`template_link.py` 和 `template_tree.py`：普通题、链表题、二叉树题各一份模板。采用一个 Cargo 项目，每道题是独立的可执行文件；不需要为每道题新建项目或手工注册模块。

## 目录

```text
rust/
├── Cargo.toml
├── src/
│   ├── lib.rs                   # 共享工具的入口，以及 list! / tree! 宏
│   ├── list.rs                  # ListNode、数组与链表互转
│   ├── tree.rs                  # TreeNode、层序数组与二叉树互转
│   └── bin/
│       └── p0001_two_sum.rs      # 已完成示例，可以立即运行、打断点
└── templates/
    ├── plain.rs                 # 普通题，以两数之和的签名占位
    ├── list.rs                  # 链表题，以反转链表的签名占位
    └── tree.rs                  # 二叉树题，以翻转二叉树的签名占位
```

`src/bin/` 下每个 `.rs` 文件都会被 Cargo 自动发现，各自有自己的 `Solution` 和 `main()`，互不冲突。文件名建议使用 `p0049_group_anagrams.rs`，需要分类时可加 `hash_` 等前缀；命令中的 `--bin` 参数就是文件名去掉 `.rs`。

## 先跑通一个示例

在仓库根目录打开终端，进入 Rust 项目：

```sh
cd rust
cargo run --bin p0001_two_sum
```

预期输出：

```text
输出结果: [0, 1]
```

运行该题的测试：

```sh
cargo test --bin p0001_two_sum
```

以下命令除特别注明外，都在 `rust/` 目录执行。项目没有第三方 Rust 依赖。

## 每天刷一道新题

1. 复制对应的模板。`cp -n` 在目标已存在时不会覆盖：

   ```sh
   # 普通题，下面以第 49 题为例
   cp -n templates/plain.rs src/bin/p0049_group_anagrams.rs

   # 链表题
   cp -n templates/list.rs src/bin/p0206_reverse_list.rs

   # 二叉树题
   cp -n templates/tree.rs src/bin/p0226_invert_tree.rs
   ```

2. 将 LeetCode 的 `impl Solution { ... }` 粘贴到文件的“提交区”，填入实现。保留文件上面的 `struct Solution;` 和本地辅助工具导入；链表、树节点已经在共享库中提供，不要重复定义。题目额外提供的自定义类型则按该题补充。

3. **同步修改 `main()` 和 `tests` 中的方法名、参数、预期输出。** Rust 是静态类型语言，换了方法签名以后，这两处调用也必须匹配。模板里的方法只是占位，`todo!()` 可以编译，执行时会报错，直到填完实现。

4. 运行当前题或测试：

   ```sh
   cargo run --bin p0049_group_anagrams
   cargo test --bin p0049_group_anagrams
   ```

5. 提交时只复制“提交区”：`impl Solution`、算法所需的标准库 `use`、以及自己写的辅助函数/类型。`struct Solution;`、本地 `use leetcode_hot100::...`、`main()`、`tests` 和共享节点定义都不用提交。设计类题目（例如 LRU Cache）可用题目给出的结构体和 `impl` 替换提交区，再在 `main()` 中依次调用操作。

未完成的其他题不会阻止 `cargo run --bin 当前题`。测试某一道题也用 `cargo test --bin 当前题`；只写测试名称过滤而不加 `--bin`，仍可能编译其他题。

## 构造与检查测试数据

### 普通数组、字符串和矩阵

```rust
let nums = vec![2, 7, 11, 15];
let text = "abcabcbb".to_string();
let matrix = vec![vec![1, 2], vec![3, 4]];
let board = vec![vec!['1', '1'], vec!['0', '1']];
```

普通数组将 LeetCode 的 `[1, 2, 3]` 改成 `vec![1, 2, 3]`；矩阵的内外层都要用 `vec!`。`String` 参数使用 `.to_string()`，字符使用单引号。

原地修改的题目在调用后检查输入：

```rust
let mut nums = vec![0, 1, 0, 3, 12];
Solution::move_zeroes(&mut nums);
assert_eq!(nums, vec![1, 3, 12, 0, 0]);
```

对于“三数之和”“字母异位词分组”等不要求输出顺序的题，先按题意排序或规范化，再使用 `assert_eq!`。

### 链表

```rust
use leetcode_hot100::{list, list_to_vec};

let head = list![1, 2, 3, 4, 5];
let empty = list![];
assert_eq!(list_to_vec(&head), vec![1, 2, 3, 4, 5]);
assert!(empty.is_none());
```

链表的类型是 `Option<Box<ListNode>>`。`list_to_vec(&head)` 借用链表，可以反复打印和断言；将 `head` 传给接收所有权的题解后，如需再次使用，重新构造即可。

### 二叉树

```rust
use leetcode_hot100::{build_tree, tree, tree_to_vec};

let root = tree![1, null, 2, 3];
assert_eq!(tree_to_vec(&root), vec![Some(1), None, Some(2), Some(3)]);

// 不使用宏时，用 Some / None 表示节点；也适合较长或动态生成的输入。
let another = build_tree(&[Some(1), None, Some(2), Some(3)]);
assert_eq!(tree_to_vec(&root), tree_to_vec(&another));
```

`tree!` 接受 LeetCode 的层序格式，支持 `null`、负数和末尾逗号。`[1, null, 2, 3]` 中 `3` 是 `2` 的左孩子；不是按完全二叉树下标构造。输出使用 Rust 的 `Some(...)` / `None`，会去掉末尾多余的 `None`。宏会递归展开，数百个节点的大输入建议直接使用 `build_tree`。

树的类型是 `Option<Rc<RefCell<TreeNode>>>`。`root.clone()` 共享原树，修改其中一份会影响另一份；需要独立测试树时重新调用 `tree!` 或 `build_tree`。

共享工具覆盖的是普通无环链表、二叉树。环形链表、相交链表、随机指针等依赖节点身份/特殊结构的题，应按该题实际提供的 Rust 接口单独建模，不能用普通数组构造器表达共享节点。

## 调试

### VS Code 断点调试

用 VS Code 打开**整个仓库根目录**（`LeetCode_Excercises/`）。配置文件放在根目录的 `.vscode/`；直接单独打开 `rust/` 不会读取它们。

需要的扩展是 `rust-lang.rust-analyzer` 和 `vadimcn.vscode-lldb`。本次检查时，本机 Rust 工具链、`rust-src`、`rustfmt`、`clippy` 和这两个扩展均已安装。

1. 打开 `rust/src/bin/p0001_two_sum.rs`，在算法内部的某一行设置断点。
2. 保持当前编辑器选中这道题的文件，在“运行和调试”下拉框中选择 **Rust：调试当前题目 main**，按 F5。
3. 用变量面板检查 `nums`、`target`、`seen` 等；单步运行查看算法过程。
4. 如需调试测试，选择 **Rust：调试当前题目 tests**。它会运行本文件所有 `#[test]`，并使用单线程，便于逐个定位。

配置使用当前文件名作为 Cargo target，所以应从 `src/bin/` 的题目文件启动。不要从 `lib.rs` 或 `templates/*.rs` 按 F5。也可以使用 rust-analyzer 在 `main` 或 `#[test]` 上方显示的 Run / Debug 按钮。

### 打印与报错定位

```rust
dbg!(&nums);                     // 带源码位置的调试输出，借用避免移动 Vec
println!("中间状态: {nums:?}");
```

测试默认隐藏通过用例的输出，加 `--nocapture` 可以直接看日志；需要调用栈时设置 `RUST_BACKTRACE`：

```sh
cargo test --bin p0001_two_sum -- --nocapture
RUST_BACKTRACE=1 cargo run --bin p0001_two_sum
```

## 常用检查

```sh
cargo fmt                           # 格式化项目中的题目与共享工具
cargo check --bin p0001_two_sum      # 只检查当前题的编译
cargo clippy --bin p0001_two_sum     # 检查常见 Rust 写法问题
cargo test --lib                    # 只测试共享工具
cargo test --all-targets            # 测试所有题目和共享工具
```

有尚未写完的题时，全量检查可能失败，先使用指定 `--bin` 的命令即可。

## 参考

- [Cargo 项目结构](https://doc.rust-lang.org/cargo/guide/project-layout.html)
- [Cargo target 与独立可执行文件](https://doc.rust-lang.org/cargo/reference/cargo-targets.html)
- [Cargo 测试与 target 选择](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [VS Code 官方 Rust 环境与调试说明](https://code.visualstudio.com/docs/languages/rust)
- [CodeLLDB 的 Cargo 调试支持](https://github.com/vadimcn/codelldb/blob/master/MANUAL.md#cargo-support)
