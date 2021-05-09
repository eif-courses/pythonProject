import pandas as pd

if __name__ == '__main__':
    file_path = 'input.html'
    with open(file_path, 'r') as f:
        dfs = pd.read_html(f.read(), keep_default_na=False, header=0)
        for i in range(1, len(dfs)):
            print(dfs[i].iloc[0, 0])