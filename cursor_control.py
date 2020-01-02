import asyncio
from cortex import Cortex
import time
import pyautogui
import json
import keyboard



cortex = Cortex("C:\\Users\\Siwen Wang\\Desktop\\Cursor_Control_V1\\cortex_creds.txt")
async def set_up(cortex):
    # await cortex.inspectApi()
    print("** USER LOGIN **")
    await cortex.get_user_login()
    print("** GET CORTEX INFO **")
    await cortex.get_cortex_info()
    print("** HAS ACCESS RIGHT **")
    await cortex.has_access_right()
    print("** REQUEST ACCESS **")
    await cortex.request_access()
    print("** AUTHORIZE **")
    await cortex.authorize()
    print("** GET LICENSE INFO **")
    await cortex.get_license_info()
    print("** QUERY HEADSETS **")
    await cortex.query_headsets()
    if len(cortex.headsets) > 0:
        print("** CREATE SESSION **")
        await cortex.create_session(activate=True,
                                    headset_id=cortex.headsets[0])
        print("** CREATE RECORD **")
        await cortex.create_record(title="test record 1")
        #print("** CREATE PROFILE **")
        #await cortex.setup_profile()
        print("** LOAD PROFILE **")
        await cortex.load_profile()
        print("** SUBSCRIBE SYSTEM **")
        await cortex.subscribe(['com'])
        while True:
            await cortex.get_data()

            thought=await cortex.get_data()
            if thought == "push":
                pyautogui.moveRel(-4,0,0)
            if keyboard.is_pressed('b'):
                break
       
        #print(thought)

        #print("** GET Detection INFO **")
        #await cortex.get_detection_info()
        #print("** Closing Session **")
        #await cortex.close_session()
        #time.sleep(5)
        #print("** Train" + " " +command +"**")
        #await cortex.training(command)
        #time.sleep(5)
        #time.sleep(5)
        #print("** Get Training Time **")
        #await cortex.get_training_time()
        #print("** Accept Training **")
        #await cortex.accept(command)
        #print("** SET MENTAL COMMAND ACTIVE ACTIONS **") 
        #await cortex.mental_command_active_action_set()
        #print("** GET MENTAL COMMAND ACTIVE ACTIONS **")
        #await cortex.mental_command_active_action_get()
        #print("** Mental Command Detected **")
        #await cortex.mental_command_brainmap()
        #await cortex. mental_command_active_action()
        
asyncio.run(set_up(cortex))

        #await cortex.mental_command_brainmap()
        #thought,coord = cortex.mental_command_brainmap()
        #if thought == "neutral":
        #    pyautogui.moveRel(4,0,1)
#start=input("To train command, please press 1; To begin game, please press 2")
#if start=="1":
#    asyncio.run(set_up(cortex,"neutral"))
#    print("Now we can start the game, note that you just trained your neutral state, and this will make your mouse cursor move left")
    





