def activecase(case_num):
    # read input from single case 
    (num_candy_bag, num_kid) =tuple(map(int, input().split()))
    candy_counts =list(map(int, input().split()))

    total =0
    for i in range(num_candy_bag):
        total += candy_counts[i]
    
    amount_remaining = total % num_kid

    print(f"case #{case_num}: {amount_remaining}")

case_num = int(input())
for i in range(case_num):
    activecase(i+1)

# lst = [1,2,3,4,5,6,7,8,9]

# it = tuple(map(int, input().split()))
# print(it)