import pandas as pd

if __name__ == '__main__':
    file_path = 'input.html'
    with open(file_path, 'r') as f:
        dfs = pd.read_html(f.read(), keep_default_na=True, header=0)
    pd.options.display.max_colwidth = 100000
    # row = dfs[i].iloc[[0]]
    row = dfs[1].iloc[:, 0]
    temp = ''
    for j in range(1, 20):
        val = dfs[1].iloc[:, j]
        temp += val + ','
        # print('' + val + ' ')
    # print('Skill(name="' + row + '")' + 'values= ' + temp)
    row.to_string(index=False)
    customObject = 'Skill(name="' + 'none' + '",description="",position=0,isEnabled=false,classname="Necromancer", levelreq="1",properties=listOf(Property(name="' + row + '",valuesByLevel="' + temp + '")),bonuses=listOf()),'
    print(row.to_string(index=False))
    f = open("demofile2.txt", "w")
    f.write(customObject.to_string(index=False))
    f.close()
# print(dfs[i].iloc[0, 0])
# print(dfs[i].iloc[1, 1:21])
