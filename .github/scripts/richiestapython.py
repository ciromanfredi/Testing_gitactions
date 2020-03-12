import requests
import sys
def main(argv):
    for i in range(5,17):
        if argv[i]<1 or argv[i]>15 or not argv[1].isnumeric():
            argv[i]=1

    if argv[4]<25 or argv[4]>29:
        argv[4]=27

    data=dict(
                radio_api=argv[4],
                text1_nevent=argv[5],
                text2_nevent=argv[6],
                text3_nevent=argv[7],
                text4_nevent=argv[8],
                text5_nevent=argv[9],
                text6_nevent=argv[10],
                text1_wtime=argv[11],
                text2_wtime=argv[12],
                text3_wtime=argv[13],
                text4_wtime=argv[14],
                text5_wtime=argv[15],
                text6_wtime=argv[16],
                email=argv[2]                                
                )

    for i in range(17,20):
        if argv[i]=="si":
            if i==17:
                data["Doc_Checkbox"]="doc"
            elif i==18:
                data["Br_Checkbox"]="bf"
            elif i==19:
                data["Stai_Checkbox"]="stai"

    response = requests.post(argv[1], 
                            data=data,
                            files=dict(
                                        myFile0=open(argv[3], 'r'),
                                        myFile1="",
                                        myFile2="",
                                        myFile3=""
                                    ),
                            verify=False
        )
    print(response.status_code)
    from pprint import pprint
    print(response.text)

if __name__ == "__main__":
   main(sys.argv[1:])