import sys as s

CIRCUIT = '.circuit'
END = '.end'

def tokens(spiceLine):
    lineWords = spiceLine.split()

    if len(lineWords) == 4:
        Name = allWords[0]
        node1 = allWords[1]
        node2 = allWords[2]
        value = allWords[3]
        return [elementName, node1, node2, value]

    elif len(lineWords) == 5:
        elementName = allWords[0]
        node1 = allWords[1]
        node2 = allWords[2]
        voltageSource = allWords[3]
        value = allWords[4]
        return [elementName, node1, node2, voltageSource, value]

    elif len(lineWords) == 6:
        elementName = allWords[0]
        node1 = allWords[1]
        node2 = allWords[2]
        voltageSourceNode1 = allWords[3]
        voltageSourceNode2 = allWords[4]
        value = allWords[5]
        return [elementName, node1, node2, voltageSourceNode1, voltageSourceNode2, value]

    else:
        return []

if len(s.argv) == 1:
    print('No inputfile detected \n Usage: %s <inputfile>' % s.argv[0])
    exit()
    
elif len(s.argv) > 2:
    print('More than one inputfile detected \n Usage: %s <inputfile>' % s.argv[0])
    exit()
    
f = open(s.argv[1],'r')
lines = f.readlines()

for line in lines:
    if CIRCUIT == line.strip():
        start = lines.index(line)
    elif END == line.strip():
        end = lines.index(line)        
try:
    for k in range(1,end-start):
        words = lines[end-k].split()
        if '#' in words:
            m = words.index('#')
            for i in range(m):
                print(words[m-i-1] + " ",end="")  
        else:
            words.reverse()
            for word in words:
                print(word + " ",end="")
        print("") 
        
    for k in range(1,end-start):
        words = lines[end-k].split()
        if '#' in words:
            m = words.index('#')
            if m == 4:
                print("Name of Element: " + words[0])
                print("Node1: " + words[1])
                print("Node1: " + words[2])
                print("Value: " + words[3])
                print("Name of Element: " + words[0])
                print("Node1: " + words[1])
                print("Node1: " + words[2])
                print("Value: " + words[3])
                
            elif m == 5:
                print("Name of Element: " + words[0])
                print("Node1: " + words[1])
                print("Node1: " + words[2])
                print("Voltage Source Node1: " + words[3])
                print("Value: " + words[4])
                
            elif m == 6:
                print("Name of Element: " + words[0])
                print("Node1: " + words[1])
                print("Node1: " + words[2])
                print("Voltage Source Node1: " + words[3])
                print("Voltage Source Node2: " + words[4])
                print("Value: " + words[5])
        else:
            
            if len(words) == 4:
                print("Name of Element: " + words[0])
                print("Node1: " + words[1])
                print("Node1: " + words[2])
                print("Value: " + words[3])
                print("Name of Element: " + words[0])
                print("Node1: " + words[1])
                print("Node1: " + words[2])
                print("Value: " + words[3])
                
            elif len(words) == 5:
                print("Name of Element: " + words[0])
                print("Node1: " + words[1])
                print("Node1: " + words[2])
                print("Voltage Source Node1: " + words[3])
                print("Value: " + words[4])
                
            elif len(words) == 6:
                print("Name of Element: " + words[0])
                print("Node1: " + words[1])
                print("Node1: " + words[2])
                print("Voltage Source Node1: " + words[3])
                print("Voltage Source Node2: " + words[4])
                print("Value: " + words[5])
        print("") 
    
    
except:
    print('Invalid circuit definition')
    exit()
        
            
        
