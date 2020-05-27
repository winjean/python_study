import os
result = []


def get_all_file(cwd):

    print(f"current dir: {cwd}")

    # 遍历当前目录，获取文件列表
    get_dir = os.listdir(cwd)
    for i in get_dir:
        # 把第一步获取的文件加入路径,获取完整的路径
        sub_dir = os.path.join(cwd, i)

        # 如果当前仍然是文件夹，递归调用
        if os.path.isdir(sub_dir):
            get_all_file(sub_dir)
        else:
            # 如果当前路径不是文件夹，则把文件名放入列表
            ax = os.path.basename(sub_dir)
            result.append(ax)


def main():
    # 当前目录
    cur_path = os.getcwd()
    get_all_file(cur_path)
    print(result)
    print(f"{'-'*10}共{len(result)}个文件{'-'*10}")


if __name__ == "__main__": 
    main()
