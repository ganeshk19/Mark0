import pandas as pd
import requests
url = "https://www.fast2sms.com/dev/bulk"

encryptionkey = pd.read_csv(r"YOUR CSV PATH",sep=',', names=['Character', 'Byte'], header=None, skiprows=[0])

df = pd.DataFrame(data=encryptionkey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)
def split(message):
    return [char for char in message]
while(True):
  a=int(input("\n1.Encryption\n2.Decryption\n3.Exit\n\nEnter Your Choice : "))
  if(a==1):
    message = input("Enter Your Message : ")
    message_split = split(message)
    def code_message():
      coded_message = ""

      for i in range(len(message_split)):
          j = message_split[i]
          try:
              coded_char = encryptionkey.loc[encryptionkey['Character'] == j, 'Byte'].iloc[0]


          # To handle if character is not in our decryption list
          except:
              print('unrecognized character')
              coded_char = '@@@'

          coded_message = coded_message + coded_char
      return coded_message
    text = code_message()
    coded_message = code_message()


    def insert_sting_middle(str, word):
    	return str[:25] + word + str[25:]
    payload = insert_sting_middle("sender_id=FSTSMS&message=&language=english&route=p&numbers=", coded_message)
    payload = payload +input("\nEnter reciever number :")
    headers = {
    'authorization': "YOUR FAST2SMS TOKEN",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    code = code_message()
    print('Your coded message:', code, '\n')
  if(a==2):
   def decode_message(message):
      new_word = ''
      decoded_message = []

      for i in range(0, len(message), 2):
          j = message[i:i + 2]
          index_nb = df[df.eq(j).any(1)]

          df2 = index_nb['Character'].tolist()

          s = [str(x) for x in df2]

          decoded_message = decoded_message + s

      new_word = ''.join(decoded_message)

      return new_word
  
   coded_message_str = input("\nEnter The Coded Message : ")
   print('Your decoded message:', decode_message(coded_message_str))
  if(a==3):
    break
  if(a>3):
    print("\n\n*********Enter Correct Choice*********\n")
