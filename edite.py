import os 

def difrent_remove_string(): 
        txt_orginal = input(str("[1- Send Me Config :  "))

        try : 
             
            LenProdVmess = len("vmess") ; sslen = len("ss") ;httpsLen = len("https") 
            if txt_orginal[0:LenProdVmess] or txt_orginal[0:sslen] or txt_orginal[0:httpsLen] == "vmess" or "ss" or "https": 
                
                LsitString = list(txt_orginal)
                listd = LsitString.index("#")
                remov = LsitString[0:listd+1]
                bmc = remov + ["✅@FreeINir"] 

                space = "".join(bmc)
                print("\n") 
                print(space)
                
                # Add To Github Config [github link : https://github.com/meahura/Freeinternet]                
                os.system("")

            else:
                print("this format not True ")
        except : 
             
             pass
            
difrent_remove_string() 


