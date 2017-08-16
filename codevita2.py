def removeComments(s):
	new = ""
	chars = "[]()<{>}@\//"
	flag = False
	i = 0
	for i in range(len(s)):
		if(s[i] not in chars):
			continue

		if(s[i] == '@'):
			if(i>0):
				if(flag and s[i-1] == '*'):
					flag = False
			if(i<len(s)):		
				if(s[i+1] == '*'):
					flag = True
			continue

		if(flag):
			continue

		new += s[i]
		i+=1

	#print(new) 
	return new

def isBalanced(s):   
    answer = ""
    if(len(s)%2 != 0):
        return False
    else:
        stack = []
        for a1 in s:            
            if(a1 == "(" or a1 == "[" or a1 == "{" or a1 == "/" or a1 == "<"):
                stack.append(a1)
            else:
                if(len(stack)>0):
                    if(a1 == ")" and stack[-1] != "("):
                        return False                
                    elif(a1 == "]" and stack[-1] != "["):
                        return False
                    elif(a1 == ">" and stack[-1] != "<"):
                        return False
                    elif(a1 == "\\" and stack[-1] != "/"):
                        return False
                    elif(a1 == "}" and stack[-1] != "{"):
                        return False
                    stack.pop()
                else:
                    return False                
        if(len(stack) == 0):
            return True
        else:
            return False



N = int(input())
for i in range(N):
	string = input()

	string = removeComments(string)

	print(isBalanced(string))