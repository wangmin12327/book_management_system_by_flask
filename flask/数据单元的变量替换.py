def main():
    cells = input().split(",")  #输入一行字符串，用逗号分隔每个单元格，cells为单元格字符串列表
    array = [None] * 26 #开辟长度为26的元素全部为None的列表，[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    visited = [False] * 26#开辟长度为26的元素全部为False的列表,[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

    for i in range(len(cells)):  #遍历输入的字符串
        array[i] = cells[i][0]   #将第i个单元格的字符串中第一个字符赋值给array[i]

    if not process_cells(cells, array, visited): #  => not process_cells(cells, array, visited) == True，则执行下面语句，
                                                 # => process_cells(cells, array, visited) == False ，则执行下面语句，
                                                 # => 第i个单元格中有一个单元格的内容，满足25行process_cell(cells[i], i, array, visited) == False
                                                 # => 执行第30行代码
                                                 # =>
        print("-1")
        return

    print_output(array)

def print_output(array):
    result = [value for value in array if value is not None and value != ""]
    output = ",".join(result)
    print(output)

def process_cells(cells, array, visited):
    for i in range(len(cells)):
        if not process_cell(cells[i], i, array, visited):  # cells[i] 表示第i个单元格中的字符串内容，i 表示第i个单元格的下标位置
            return False
    return True

def process_cell(cell, index, array, visited):  # cell=cells[i],是某个单元格中的内容:asew<x>swqd
    result = cell
    while "<" in result:    # 输入的字符串中带"<"符号
        start = result.find("<") #找到结果中"<"字符第一次出现的下标地址
        end = result.find(">") #找到结果中">"字符第一次出现的下标地址

        if start == -1 or end == -1:  #如果'<' 或 '>'的第一个起始下标位置是单元格中字符串的最后一位，单元格内容违法，遍历结束
            break

        ref = result[start + 1:end] #获取<x>中x的值

        if not is_valid_reference(ref, index, array) or visited[ord(ref) - ord('A')]: # => not is_valid_reference(ref, index, array) == True
            return False    #单元格内容违法，遍历结束                                      # => is_valid_reference(ref, index, array) == False
                                                                                      # 跳到第52行
                                                                                      # 或者 visited[ord(ref) - ord('A')] == True

        visited[ord(ref) - ord('A')] = True #检查第三种非法情况，A :<B>     B :
        result = result[:start] + array[ord(ref) - ord('A')] + result[end + 1:] #将检查好格式的单元格内容，并且将单元格数据单元替换后，赋值给result

    array[index] = result # 将result值赋给第i个单元格
    return True

def is_valid_reference(ref, index, array):  #只有下列情况中都为True，才能确保第i个单元格的内容合法
    return (
        len(ref) == 1  #切片，包含起始下标，确保<x>中x的长度为1
        and ref.isupper() #确保<x>中的x是大写字母
        and index != ord(ref) - ord('A') # index为某个单元格的下标，确保第一种非法情况不会出现： A :aCd<B>8u  B :kAy<A>dzqo
        and array[ord(ref) - ord('A')] is not None #确保第二种非法情况不会出现: A :<B>    B :<A>
    )

if __name__ == "__main__":
    main()

