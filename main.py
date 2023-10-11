        START = False

        PUBBLIC = False
        
        LINK = ""

        VELOCITY_REJOIN = 14
        
        QUITTER = False

        MINUTES = 0

        ONLINE = True

        FLUXUS = False
        KRNL = False

        krnlPATH = ""
        
        fluxusPATH = ""
        
        def load_path_data(name):
            global krnlPATH,fluxusPATH,entryPath,entryPath2
            STOKEF()
            
            if name == "krnl":
                if krnlPATH == "":
                    messagebox.showwarning("Empty Data","The Data Is Empty")
                else:
                    entryPath.delete(0,t.END)
                    entryPath.insert(0, krnlPATH)
                    
            elif name == "flux":
                if fluxusPATH == "":
                    messagebox.showwarning("Empty Data","The Data Is Empty")
                else:
                    entryPath2.delete(0,t.END)
                    entryPath2.insert(0, fluxusPATH)
                    
            else:
                messagebox.showerror("ERROR 033", "error no execL")
            
        
        def store_paths_ex(executorName):
            global entrySave, krnlPATH,fluxusPATH
            gotten = entrySave.get()
            if executorName == "KRNL":
                krnlPATH = gotten
            elif executorName == "FLUXUS":
                fluxusPATH = gotten
            else:messagebox.showerror("ERROR 032", "error no exec")
            entrySave.delete(0, t.END)
            STOKEF()
            
        def STOKEF():
            def secondACT():
                global fluxusPATH, krnlPATH
                if os.path.exists("Data/ExecPaths.pkl"):
                    with open("./Data/ExecPaths.pkl", "rb") as dataFile:
                        data : list = pickle.load(dataFile)
                                    
                        with open("./Data/ExecPaths.pkl", "wb") as fil:
                            if krnlPATH == "":
                                krnlPATH = data[0]
                            if fluxusPATH == "":
                                fluxusPATH = data[1]
                            
                            pickle.dump(obj=(krnlPATH,fluxusPATH), file=fil)
                            fil.close()
                        fil.close()
                        dataFile.close()
                    dataFile.close()
                else:
                    with open("Data/ExecPaths.pkl", "wb") as dataFile:
                        pickle.dump(obj=(krnlPATH,fluxusPATH), file=dataFile)
                        dataFile.close()
                    dataFile.close()
            
            
            if os.path.exists("Data"):
                secondACT()
            
            else:
                os.mkdir("Data")
                secondACT()
        
        def bg_color_set(color):
            global tabs
            tabs.configure(bg_color=color)
        
        def fg_color_set(color):
            global tabs
            tabs.configure(fg_color=color)
        
        def fg_Main_color_set(color):
            global tabs
            tabs.tab("ReloaderSW").configure(fg_color=color)
        
        def fg_ExecSW_color_set(color):
            global tabs
            tabs.tab("AR_Executor").configure(fg_color=color)
        
        def fg_Theme_color_set(color):
            global tabs
            tabs.tab("ThemeSW").configure(fg_color=color)
        
        def default_bg_color():
            global COLORG ,tabs
            COLORG = "#8200c9"
            tabs.configure(bg_color=COLORG)
        
        def default_fg_color():
            global COLORF ,tabs
            COLORF = "purple"
            tabs.configure(fg_color=COLORF)
        
        def default_fg_Main_color():
            global tabs
            tabs.tab("ReloaderSW").configure(fg_color="purple")
        
        def default_fg_ExecSW_color():
            global tabs
            tabs.tab("AR_Executor").configure(fg_color="purple")
        
        def default_fg_Theme_color():
            global tabs
            tabs.tab("ThemeSW").configure(fg_color="purple")
        
        def default_theme():
            global COLORF,COLORG,TEXT_COLOR,SEG_BUT_FG_C,SEG_BUT_SEL_C,SEG_BUT_SEL_HOV_C,SEG_BUT_UNSEL_C,SEG_BUT_UNSEL_HOV_C, tabs
            COLORF= "purple"
            COLORG="#8200c9"
            TEXT_COLOR = "#98ff4e"
            SEG_BUT_FG_C = "#060819"
            SEG_BUT_SEL_C = "#9a26ff"
            SEG_BUT_SEL_HOV_C = "#2e0b4c"
            SEG_BUT_UNSEL_C  = "#cc92ff"
            SEG_BUT_UNSEL_HOV_C  = "#ae51ff"

            tabs.configure(text_color=TEXT_COLOR, bg_color=COLORG, fg_color=COLORF,
                            segmented_button_fg_color=SEG_BUT_FG_C, segmented_button_selected_color=SEG_BUT_SEL_C,segmented_button_selected_hover_color=SEG_BUT_SEL_HOV_C,
                            segmented_button_unselected_color=SEG_BUT_UNSEL_C,segmented_button_unselected_hover_color=SEG_BUT_UNSEL_HOV_C)
    
        def submitFP():
            global entryPath2,fluxusPATH
            GotPath = entryPath2.get()
            fluxusPATH = GotPath
        
        def submitKP():
            global entryPath,krnlPATH
            GotPath = entryPath.get()
            krnlPATH = GotPath

        def executorON_OFFFLUXUS():
            global FluxusSwitch,FLUXUS
            if FluxusSwitch.get() == 1:
                FLUXUS = True
            elif FluxusSwitch.get() == 0:
                FLUXUS = False
            else:
                messagebox.showerror("Error EF", "E::FLUXUS Bug")
       
        def executorON_OFFKRNL():
            global krnlSwitch, KRNL
            if krnlSwitch.get() == 1:
                KRNL = True
            elif krnlSwitch.get() == 0:
                KRNL = False
            else:
                messagebox.showerror("Error EK", "E::KRNL Bug")

        def executor_rejoinedFLUXUS():
            global FLUXUS ,fluxusPATH
            pathF = rf"{fluxusPATH}"  
            if FLUXUS == True:  
                if check_if_process_running("FluxusV7.exe"):
                    try:os.system('taskkill /f /im FluxusV7.exe')
                    except:pass
                    
                    try:os.system(f"start {pathF}")
                    except:pass
                else:
                    try:os.system(f"start {pathF}")
                    except:pass
            else:pass
        
        def executor_rejoinedKRNL():
            global KRNL,krnlPATH
            pathK = rf"{krnlPATH}"
            if KRNL == True:
                if check_if_process_running("krnl.exe"):
                    try:os.system('taskkill /f /im krnl.exe')
                    except:pass
                    try:os.system(f"start {pathK}")
                    except:pass
                else:
                    try:os.system(f"start {pathK}")
                    except:pass
            else:pass
        
        def updatequitterMINS():
            global MINUTES
            global quitterSC
            quitterSC.clear()
            quitterSC.every(MINUTES).minutes.do(FORCEapple)

        def updatemainVel():
            global MainReSC, VELOCITY_REJOIN
            MainReSC.clear()
            MainReSC.every(VELOCITY_REJOIN).seconds.do(upd_status)

        def setMinutes(minutes):
            global MINUTES
            MINUTES = minutes
            
        def quitterSWITCH():
            global switchQuitter,QUITTER
            if switchQuitter.get() == 1:
                QUITTER = True
            elif switchQuitter.get() == 0:
                QUITTER = False
            else:
                messagebox.showerror("Error Q", "Quitter Bug")
     
        def ConvUpdate():
                def secondpart():
                    global STOREDUSER, STOREDPASS, STOREDPS1, STOREDID1, STOREDPS2, STOREDID2
                    if os.path.exists("Data/SavedData.pkl"):
                        with open("./Data/SavedData.pkl", "rb") as dataFile:
                            data : list = pickle.load(dataFile)
                                        
                            with open("./Data/SavedData.pkl", "wb") as fil:
                                if STOREDUSER == "":
                                    STOREDUSER = data[0]
                                if STOREDPASS == "":
                                    STOREDPASS = data[1]
                                if STOREDPS1 == "":
                                    STOREDPS1 = data[2]
                                if STOREDID1 == "":
                                    STOREDID1 = data[3]
                                if STOREDPS2 == "":
                                    STOREDPS2 = data[4]
                                if STOREDID2 == "":
                                    STOREDID2 = data[5]
                                                
                                pickle.dump(obj=(STOREDUSER, STOREDPASS, STOREDPS1, STOREDID1, STOREDPS2, STOREDID2), file=fil)
                                fil.close()
                            fil.close()
                            dataFile.close()
                        dataFile.close()
                    else:
                        with open("./Data/SavedData.pkl", "wb") as dataFile:
                            pickle.dump(obj=(STOREDUSER, STOREDPASS, STOREDPS1, STOREDID1, STOREDPS2, STOREDID2), file=dataFile)
                            dataFile.close()
                        dataFile.close()
                
                if os.path.exists("Data"):
                    secondpart()
    
                else:
                    os.mkdir("Data")
                    secondpart()  
                    
        def PS1UPDATE():
            global STOREDPS1
            global LINK
            ConvUpdate()
            if STOREDPS1 == "":
                messagebox.showwarning("Empty Data","The Data Is Empty")
            else:
                GetPsLinkENTRY.delete(0,t.END)
                GetPsLinkENTRY.insert(0, STOREDPS1)
                LINK = STOREDPS1
                    
        def PS2UPDATE():
            global STOREDPS2  
            global LINK  
            ConvUpdate()
            if STOREDPS2 == "":
                messagebox.showwarning("Empty Data","The Data Is Empty")
            else:
                GetPsLinkENTRY.delete(0,t.END)
                GetPsLinkENTRY.insert(0, STOREDPS2)
                LINK = STOREDPS2
                
        def ID1UPDATE():
            global STOREDID1
            global ID
            ConvUpdate()
            if STOREDID1 == "":
                messagebox.showwarning("Empty Data","The Data Is Empty")
            else:
                GetIDRoblox.delete(0,t.END)
                GetIDRoblox.insert(0, STOREDID1)
                try:
                    ID = int(STOREDID1)
                except:
                    messagebox.showerror("Type?", "Are You Sure You Typed Only Numbers For The ID?")
                
        def ID2UPDATE():
            global STOREDID2
            global ID
            ConvUpdate()
            if STOREDID2 == "":
                messagebox.showwarning("Empty Data","The Data Is Empty")
            else:
                GetIDRoblox.delete(0,t.END)
                GetIDRoblox.insert(0, STOREDID2)
                try:
                    ID = int(STOREDID2)
                except:
                    messagebox.showerror("Type?", "Are You Sure You Typed Only Numbers For The ID?")
            
        def PLANT_ID():
            global ID
            ID = int(GetIDRoblox.get())
            
        def PLANT_LINK():
            global LINK
            LINK = GetPsLinkENTRY.get()

        def ChoseMode():
            global VELOCITY_REJOIN
            CURRENT = RadioVar.get()
            if CURRENT == "0":
                VELOCITY_REJOIN = 20
            elif CURRENT == "1":
                VELOCITY_REJOIN = 14
            elif CURRENT == "2":
                VELOCITY_REJOIN = 10
            elif CURRENT == "3":
                VELOCITY_REJOIN = 7
            elif CURRENT == "4":
                VELOCITY_REJOIN = 5

        def DataScreen():
            def FinalStore():
                def secondpart():
                    global STOREDUSER, STOREDPASS, STOREDPS1, STOREDID1, STOREDPS2, STOREDID2
                    if os.path.exists("Data/SavedData.pkl"):
                        with open("./Data/SavedData.pkl", "rb") as dataFile:
                            data : list = pickle.load(dataFile)
                                        
                            with open("./Data/SavedData.pkl", "wb") as fil:
                                if STOREDUSER == "":
                                    STOREDUSER = data[0]
                                if STOREDPASS == "":
                                    STOREDPASS = data[1]
                                if STOREDPS1 == "":
                                    STOREDPS1 = data[2]
                                if STOREDID1 == "":
                                    STOREDID1 = data[3]
                                if STOREDPS2 == "":
                                    STOREDPS2 = data[4]
                                if STOREDID2 == "":
                                    STOREDID2 = data[5]
                                                
                                pickle.dump(obj=(STOREDUSER, STOREDPASS, STOREDPS1, STOREDID1, STOREDPS2, STOREDID2), file=fil)
                                fil.close()
                            fil.close()
                            dataFile.close()
                        dataFile.close()
                    else:
                        with open("./Data/SavedData.pkl", "wb") as dataFile:
                            pickle.dump(obj=(STOREDUSER, STOREDPASS, STOREDPS1, STOREDID1, STOREDPS2, STOREDID2), file=dataFile)
                            dataFile.close()
                        dataFile.close()
                
                if os.path.exists("Data"):
                    secondpart()
                
                else:
                    os.mkdir("Data")
                    secondpart()  
            
            def StoreName():
                global STOREDUSER
                STOREDUSER = str(StoreDataEntry.get())
                StoreDataEntry.delete(0, t.END)          
            def StorePass():
                global STOREDPASS
                STOREDPASS = str(StoreDataEntry.get())
                StoreDataEntry.delete(0, t.END)       
            def StorePS1():
                global STOREDPS1
                STOREDPS1 = str(StoreDataEntry.get())
                StoreDataEntry.delete(0, t.END)     
            def StoreID1():
                global STOREDID1
                STOREDID1 = str(StoreDataEntry.get())
                StoreDataEntry.delete(0, t.END)            
            def StorePS2():
                global STOREDPS2
                STOREDPS2 = str(StoreDataEntry.get())
                StoreDataEntry.delete(0, t.END)              
            def StoreID2():
                global STOREDID2
                STOREDID2 = str(StoreDataEntry.get())
                StoreDataEntry.delete(0, t.END)
            
            def showsavesxD():
                global STOREDUSER, STOREDPASS, STOREDPS1, STOREDID1, STOREDPS2, STOREDID2
                def kj():
                    showD.destroy()
                    ShowSaves.configure(state="normal")
                
                def updatedata():
                    global STOREDUSER, STOREDPASS, STOREDPS1, STOREDID1, STOREDPS2, STOREDID2
                    FinalStore()
                    TextBox.configure(state="normal")
                    TextBox.delete(0.0, t.END)
                    TextBox.insert(0.0, f"UserName Saved: {STOREDUSER}\nPassWord Saved: {STOREDPASS}\nPS1 Saved: {STOREDPS1}\nID1 Saved: {STOREDID1}\nPS2 Saved: {STOREDPS2}\nID2 Saved: {STOREDID2}\n")
                    TextBox.configure(state="disabled")
                    
                    
                ShowSaves.configure(state="disabled")
                
                showD = t.CTk()
                showD.title("Data Show")
                
                w = 350
                h = 180
                ws = showD.winfo_screenwidth()
                hs = showD.winfo_screenheight()
                x = (ws/2) - (w/.5)
                y = (hs/1.8) - (h/2.8)
            
                showD.geometry('%dx%d+%d+%d' % (w, h, x, y))
                
                
                # id2.geometry("350x180")
                showD.resizable(False,False)
                showD._set_appearance_mode("dark")
                showD.protocol("WM_DELETE_WINDOW", kj)

                id = "mycompany.myproduct.subproduct.version"
                ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(id)

                showD.iconbitmap(appleRaw)

                backgroundD2 = t.CTkFrame(showD, border_color="yellow", border_width=3, bg_color="#d28fec", fg_color="#c1cdc1",corner_radius=30)
                backgroundD2.pack(fill= "both", expand=1)


                TextBox = t.CTkTextbox(backgroundD2,text_color="yellow", bg_color="#242424", fg_color="purple", font=("Calibri",16), height=120,width=350 ,scrollbar_button_color="blue", scrollbar_button_hover_color="darkblue", border_color="yellow", border_width=3)
                TextBox.insert(0.0, f"UserName Saved: {STOREDUSER}\nPassWord Saved: {STOREDPASS}\nPS1 Saved: {STOREDPS1}\nID1 Saved: {STOREDID1}\nPS2 Saved: {STOREDPS2}\nID2 Saved: {STOREDID2}\n")
                TextBox.configure(state="disabled")
                TextBox.place(x=0,y=0)
                
                updateshow = t.CTkButton(backgroundD2, text_color="red", bg_color="#242424", fg_color="green", text="Update Show Data", border_color="yellow", border_width=3, command=updatedata)
                updateshow.place(x=0,y=150)
                
                showD.mainloop()
            
            def hjk():
                try:
                    datas.destroy()
                    SaveDataButton.configure(state="normal")
                except: pass
            
            SaveDataButton.configure(state="disabled")
            
            datas = t.CTk()
            datas.title("DataSW Save")
            w = 280
            h = 500
            ws = datas.winfo_screenwidth()
            hs = datas.winfo_screenheight()
            x = (ws/1) - (w/.5)
            y = (hs/2) - (h/3)
            
            datas.geometry('%dx%d+%d+%d' % (w, h, x, y))
            
            # datas.geometry("280x500")
            datas.resizable(False,False)
            datas.protocol("WM_DELETE_WINDOW", hjk)
            datas._set_appearance_mode("dark")
            
            id = "mycompany.myproduct.subproduct.version"
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(id)

            datas.iconbitmap(appleRaw)
            
            backgroundD1 = t.CTkFrame(datas, border_color="darkblue", border_width=3, bg_color="#d28fec", fg_color="#ff2345",corner_radius=30)
            backgroundD1.pack(fill="both", expand=1)
            
            
            info = t.CTkTextbox(backgroundD1,border_color="black", border_width=2 ,text_color="red", bg_color="transparent", fg_color="blue",corner_radius=25,scrollbar_button_color="blue", scrollbar_button_hover_color="darkblue",width=240,font=("Calibri", 17))
            info.insert(0.0, "INFORMATION\n\nInsert Data And\nClick The Button\nWhich You Want\nTo Store.\nRemember To Save!\n\nEnjoy!\nBy AppleSW.")
            info.configure(state="disabled")
            info.place(x=20,y=0)
            
            label = t.CTkLabel(backgroundD1, text_color="black", text="Data To Store:")
            label.place(x=5,y=210)
            
            StoreDataEntry = t.CTkEntry(backgroundD1, text_color="#20ffff", width=220,height=30,corner_radius=20,fg_color="#7f7d00",font=("Calibri", 14))
            StoreDataEntry.place(x=30,y=240)
            
            text_color_1 = "#fffb32"
            width_S,height_S = 50,20
            
            
            UserNameStore = t.CTkButton(backgroundD1, text="Store UserName",
                                        text_color=text_color_1,
                                        bg_color="transparent",
                                        fg_color="green",
                                        border_color="yellow",
                                        border_width=2,
                                        hover_color="darkgreen",
                                        command=StoreName,
                                        width=width_S,
                                        height=height_S)
            PassWordStore = t.CTkButton(backgroundD1, text="Store PassWord",
                                        text_color=text_color_1,
                                        bg_color="transparent",
                                        fg_color="green",
                                        border_color="yellow",
                                        border_width=2,
                                        hover_color="darkgreen",
                                        command=StorePass,
                                        width=width_S,
                                        height=height_S)
            
            
            PrivateLinkStore1 = t.CTkButton(backgroundD1, text="Store PrivateLink 1",
                                        text_color=text_color_1,
                                        bg_color="transparent",
                                        fg_color="green",
                                        border_color="yellow",
                                        border_width=2,
                                        hover_color="darkgreen",
                                        command=StorePS1,
                                        width=width_S,
                                        height=height_S)
            PlayerIDStore1 = t.CTkButton(backgroundD1, text="Store Player ID 1",
                                        text_color=text_color_1,
                                        bg_color="transparent",
                                        fg_color="green",
                                        border_color="yellow",
                                        border_width=2,
                                        hover_color="darkgreen",
                                        command=StoreID1,
                                        width=width_S,
                                        height=height_S)
            
            
            PrivateLinkStore2 = t.CTkButton(backgroundD1, text="Store PrivateLink 2",
                                        text_color=text_color_1,
                                        bg_color="transparent",
                                        fg_color="green",
                                        border_color="yellow",
                                        border_width=2,
                                        hover_color="darkgreen",
                                        command=StorePS2,
                                        width=width_S,
                                        height=height_S)
            PlayerIDStore2 = t.CTkButton(backgroundD1, text="Store Player ID 2",
                                        text_color=text_color_1,
                                        bg_color="transparent",
                                        fg_color="green",
                                        border_color="yellow",
                                        border_width=2,
                                        hover_color="darkgreen",
                                        command=StoreID2,
                                        width=width_S,
                                        height=height_S)
                
            Saveb = t.CTkButton(backgroundD1, text="Save",
                                        bg_color="transparent",
                                        fg_color="blue",
                                        border_color="yellow",
                                        border_width=2,
                                        hover_color="darkblue",
                                        command=FinalStore,
                                        width=150,
                                        height=26)
            
            ShowSaves = t.CTkButton(backgroundD1, text="Show Saves",
                                        bg_color="transparent",
                                        fg_color="orange",
                                        border_color="yellow",
                                        border_width=2,
                                        hover_color="green",
                                        command=showsavesxD,
                                        width=110,
                                        height=23,
                                        text_color="black")
                                        
            UserNameStore.place(x=10, y=280)
            PassWordStore.place(x=140, y=280)
            PrivateLinkStore1.place(x=10, y=330)
            PlayerIDStore1.place(x=140, y=330)
            PrivateLinkStore2.place(x=10, y=380)
            PlayerIDStore2.place(x=140, y=380)
            
            Saveb.place(x=60,y=400)
            ShowSaves.place(x=20, y=450)
            
            datas.mainloop()
            
        def UpdateNseeStatus():
            status.destroy()
            createSta()

        def createSta():
            global START
            global PUBBLIC
            status = t.CTkLabel(master_under,
                            text=f"Status: {START}",
                            height=15)
            status.place(x=240, y=215)
               
        def upd_status():
            updatemainVel()
            apple()
            
        def PuBON_OFf():
            global PUBBLIC
            if var_public.get() == "on":
                PUBBLIC = True
            elif var_public.get() == "off":
                PUBBLIC = False
            else:pass
            
            status.destroy()
            createSta()
                  
        def FORCEapple():
            global START
            global LINK
            global PUBBLIC
            global QUITTER
            updatequitterMINS()
            if QUITTER:
                def forceKILL():
                    try:
                        for process in psutil.process_iter():
                            try:
                                if process.name() == "Windows10Universal.exe":
                                    try:
                                        os.system(f'taskkill /f /im  {process.pid}')
                                    except:pass
                                    try:
                                        process.kill()
                                    except:pass
                            except:pass
                    except:pass
                
                forceKILL()
                
                if START == True:
                    if PUBBLIC == True:
                        # click.launch("roblox://placeID=536102540")
                        webbrowser.open("roblox://placeID=536102540", autoraise=False)

                        
                    else:
                        # click.launch(LINK)
                        webbrowser.open(LINK, autoraise=False)
                        
                    
                    if check_if_process_running("msedge.exe"):
                        os.system("taskkill /f /im msedge.exe")
                    else: pass
                                
                else: pass
            else:pass
        
        def apple():
            global START
            global ID
            global LINK
            global PUBBLIC
            
            if START == True:
                if PUBBLIC == True:

                    
                    headers = {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    }

                    data = {
                        "userIds": [
                            ID 
                        ]
                    }

                    
                    
                    response = requests.post('https://presence.roblox.com/v1/presence/users', headers=headers, data=json.dumps(data))
                    st_o = response.text[38] # 38 

                    if st_o == "2": pass
                    
                    else:
                        # click.launch("roblox://placeID=536102540")
                        webbrowser.open("roblox://placeID=536102540", autoraise=False)

                    
                else:

                    
                    headers = {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    }

                    data = {
                        "userIds": [
                            ID 
                        ]
                    }

                    
                    
                    response = requests.post('https://presence.roblox.com/v1/presence/users', headers=headers, data=json.dumps(data))
                    st_o = response.text[38] # 38 

                    if st_o == "2": pass
                    
                    else:
                        webbrowser.open(LINK, autoraise=False)
                        # click.launch(LINK)
                    
                
                if check_if_process_running("msedge.exe"):
                    os.system("taskkill /f /im msedge.exe")
                else: pass
                        
                    
                    
            else: pass

        def Off_On():
            global START
            START = not START
            UpdateNseeStatus()
            upd_status()
            
        def term():
            try:
                window.destroy()
                os.system(f'taskkill /f /im   {os.getpid()}')
            except:pass

        window = t.CTk()
        window.title("𝓐𝓾𝓽𝓸𝓡𝓮𝓵𝓸𝓭𝓮𝓻 𝓥2.5.5")
        
        w = 1050
        h = 355
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        
        window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # window.geometry("800x250")
        window.resizable(False, False)
        window._set_appearance_mode("dark")
        window.protocol("WM_DELETE_WINDOW", term)
        
        # window.eval('tk::PlaceWindow . center')

        appleRaw = res_path("apple.ico")

        als = "mycompany.myproduct.subproduct.version"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(als)

        
        window.iconbitmap(appleRaw)

        
        COLORF= "purple" #fg_color
        
        COLORG="#8200c9" #bg_color
        
        B_COLOR = "green"
        
        B_WIDTH = 4 
        C_RADIUS = 40
        
        TEXT_COLOR = "#98ff4e" #text_color
        SEG_BUT_FG_C = "#060819" #segmented_button_fg_color
        
        SEG_BUT_SEL_C = "#9a26ff" #segmented_button_selected_color
        SEG_BUT_SEL_HOV_C = "#2e0b4c" #segmented_button_selected_hover_color
        
        SEG_BUT_UNSEL_C  = "#cc92ff" #segmented_button_unselected_color
        SEG_BUT_UNSEL_HOV_C  = "#ae51ff" #segmented_button_unselected_hover_color
        
        
        tabs = t.CTkTabview(window,text_color=TEXT_COLOR,border_color=B_COLOR, border_width=B_WIDTH, corner_radius=C_RADIUS, bg_color=COLORG, fg_color=COLORF,
                            segmented_button_fg_color=SEG_BUT_FG_C, segmented_button_selected_color=SEG_BUT_SEL_C,segmented_button_selected_hover_color=SEG_BUT_SEL_HOV_C,
                            segmented_button_unselected_color=SEG_BUT_UNSEL_C,segmented_button_unselected_hover_color=SEG_BUT_UNSEL_HOV_C)
        tabs.add("ReloaderSW")
        tabs.add("AR_Executor")
        tabs.add("ThemeSW")
        tabs.pack(fill="both",expand=1)
        
        tabs.tab("ThemeSW").configure(border_color="black",border_width=2,corner_radius=0)
        tabs.tab("AR_Executor").configure(border_color="black",border_width=2,corner_radius=0)
        tabs.tab("ReloaderSW").configure(border_color="black",border_width=2,corner_radius=0)
        master_under = tabs.tab("ReloaderSW")#YES
        
        
        credit = t.CTkLabel(master_under, text="Made By AppleSW",
                            corner_radius=20,
                            bg_color="transparent",
                            fg_color="red",
                            text_color="darkblue",
                            )
        credit.place(x=10, y=10)

       
        status = t.CTkLabel(master_under,
                            text=f"Status: {START}",
                            height=15)
        status.place(x=240, y=215)


        apple_button_img = t.CTkImage(Image.open(res_path("apple.ico")), size=(32,32))

        apple_button_imgV2 = t.CTkImage(Image.open(res_path("apple.ico")), size=(40,40))
        
        infoPslink = t.CTkLabel(master_under, text="Paste Your Private Link: ",font=("Calibri", 15))
        infoPslink.place(x=10, y=40)

        GetPsLinkENTRY = t.CTkEntry(master_under, text_color="#0d1133", width=170,height=35,corner_radius=20,fg_color="#61ffcf")
        GetPsLinkENTRY.place(x=70, y=70)
        GetPsLinkENTRY.bind("<Return>", lambda e : PLANT_LINK())

        psONEB = t.CTkButton(master_under,image=apple_button_imgV2, text="", width=1, height=1, corner_radius=50, bg_color="transparent", fg_color="transparent", hover=False, anchor=t.CENTER, command=PS1UPDATE) #PS1
        psONEB.place(x=250,y=59)
        
        psTWOB = t.CTkButton(master_under, image=apple_button_imgV2, text="", width=1, height=1, corner_radius=50, bg_color="transparent", fg_color="transparent", hover=False, anchor=t.CENTER, command=PS2UPDATE) #PS2
        psTWOB.place(x=310,y=59)

        psONEL = t.CTkLabel(master_under, text="Ps1", text_color="red", fg_color="darkblue", bg_color="transparent", width=23, corner_radius=50,height=13)
        psTWOL = t.CTkLabel(master_under, text="Ps2", text_color="red", fg_color="darkblue", bg_color="transparent", width=23, corner_radius=50,height=13)

        psONEL.place(x=255,y=40)
        psTWOL.place(x=315,y=40)



        infoIDRoblox = t.CTkLabel(master_under, text="Paste Your Profile Id: ",font=("Calibri", 15))
        infoIDRoblox.place(x=10, y=105)

        GetIDRoblox = t.CTkEntry(master_under, text_color="#0d1133", width=170,height=35,corner_radius=20,fg_color="#61ffcf")
        GetIDRoblox.place(x=70, y=135)
        GetIDRoblox.bind("<Return>", lambda e: PLANT_ID())


        idONEB = t.CTkButton(master_under, image=apple_button_imgV2, text="", width=1, height=1, corner_radius=50, bg_color="transparent", fg_color="transparent", hover=False, anchor=t.CENTER, command=ID1UPDATE) #ID1
        idONEB.place(x=250,y=125)
        
        idTWOB = t.CTkButton(master_under, image=apple_button_imgV2, text="", width=1, height=1, corner_radius=50, bg_color="transparent", fg_color="transparent", hover=False, anchor=t.CENTER, command=ID2UPDATE) #ID2
        idTWOB.place(x=310,y=125)

        idONEL = t.CTkLabel(master_under, text="ID1", text_color="red", fg_color="darkblue", bg_color="transparent", width=23, corner_radius=50,height=13)
        idTWOL = t.CTkLabel(master_under, text="ID2", text_color="red", fg_color="darkblue", bg_color="transparent", width=23, corner_radius=50,height=13)

        idONEL.place(x=255,y=110)
        idTWOL.place(x=315,y=110)



        meh = t.CTkTextbox(master_under, text_color="#32ffff", corner_radius=30, bg_color="transparent", fg_color="#6562b1", border_color="#07061c", border_spacing=4, border_width=4, font=("Calibri", 16), scrollbar_button_color="darkblue", scrollbar_button_hover_color="blue",width=200,height=194)

        meh.insert(t.END, "INFORMATION:\nREAD ALL!\n\nBe Sure To Click \nEnter In Both!\nAnd Dont Click Start Before You Are Sure About \nYour Id roblox And\nThe Ps Link!\n\nTo Use The\nPublic Mode\nJust Check The\nCircle.\nRemember To\nInsert The\nPlayer ID!\n\nYou Will Not Be\nAble To Use Edge\nWith This\nVersion!\n\nEvery Mode\nMeans One\nVelocity To\nOpen Roblox.\n\nThe Apple Buttons\nAre The Stored\nData You Did\nIn The Data\nSection.\n\nThe Quitter\nWill Make You\nQuit Every\nX Min.\nTo Use The\nQuitter You\nMust Turn ON.\n\nAR_Executor\nSection Is To\nReload The\nExecutor.\nThe Only Data You\nHave To Insert Is\nThe Path Of The\nExe Executor\n(Not In \" \" ).\nMust Put The Path\nBefore You Start.\n\nEnjoy!\nBy AppleSW.")
        meh.configure(state=t.DISABLED)
        meh.place(x=750, y=40)



        Startbutton = t.CTkButton(master_under, text="𝚂𝚝𝚊𝚛𝚝",
                                corner_radius=20,
                                bg_color="transparent",
                                fg_color="black",
                                text_color="yellow",
                                hover=True,
                                hover_color="darkblue",
                                command=Off_On,
                                border_color="#7b68ee",
                                border_width=3,
                                width=140,
                                height=30,
                                font=("Calibri", 20))
        Startbutton.place(x=210, y=180)
        
        var_public = t.StringVar(value="off")
        publicBoxC = t.CTkCheckBox(master_under, text="𝗣𝘂𝗯𝗹𝗶𝗰 𝗝𝗼𝗶𝗻", command=PuBON_OFf,
                                     variable=var_public, onvalue="on", offvalue="off",
                                     fg_color="darkblue",
                                     bg_color="transparent",
                                     border_color="yellow",
                                     border_width=2,
                                     corner_radius=30,
                                     width=110,
                                     height=27,
                                     font=("Calibri", 16)
                                     )
        publicBoxC.place(x=90,y=187)
        
        
        SectionMode = t.CTkLabel(master_under,text="𝓜𝓸𝓭𝓮𝓼", text_color="black", fg_color="#393cff", bg_color="transparent", corner_radius=20, font=("Calibri", 24),width=100,height=16)    
        SectionMode.place(x=415, y=5)
        RadioVar = t.StringVar(master_under, value=1)
        color_yel = "#fffb00"
        
        SlowMode = t.CTkRadioButton(master_under,text="𝗦𝗹𝗼𝘄 𝗠𝗼𝗱𝗲", command=ChoseMode, variable=RadioVar, value=0,
                                    corner_radius=50, bg_color="transparent",
                                    text_color=color_yel,
                                    radiobutton_height=20,
                                    radiobutton_width=45,
                                    border_width_checked=3,
                                    border_color="black",
                                    border_width_unchecked=3,
                                    fg_color="yellow",
                                    hover_color="green",
                                    hover=True,
                                    font=("Calibri", 16)
                                    )
        SlowMode.place(x=400, y=40)

        NormalMode = t.CTkRadioButton(master_under,text="𝗡𝗼𝗿𝗺𝗮𝗹 𝗠𝗼𝗱𝗲", command=ChoseMode, variable=RadioVar, value=1,
                                    corner_radius=50, bg_color="transparent",
                                    text_color=color_yel,
                                    radiobutton_height=20,
                                    radiobutton_width=45,
                                    border_width_checked=3,
                                    border_color="black",
                                    border_width_unchecked=3,
                                    fg_color="yellow",
                                    hover_color="green",
                                    hover=True,
                                    font=("Calibri", 16)
                                    )
        NormalMode.place(x=400, y=80)
        
        FastMode1 = t.CTkRadioButton(master_under,text="𝗙𝗮𝘀𝘁 𝗠𝗼𝗱𝗲 𝗜", command=ChoseMode, variable=RadioVar, value=2,
                                    corner_radius=50, bg_color="transparent",
                                    text_color=color_yel,
                                    radiobutton_height=20,
                                    radiobutton_width=45,
                                    border_width_checked=3,
                                    border_color="black",
                                    border_width_unchecked=3,
                                    fg_color="yellow",
                                    hover_color="green",
                                    hover=True,
                                    font=("Calibri", 16)
                                    )
        FastMode1.place(x=400, y=120)
        
        FastMode2 = t.CTkRadioButton(master_under,text="𝗙𝗮𝘀𝘁 𝗠𝗼𝗱𝗲 𝗜𝗜", command=ChoseMode, variable=RadioVar, value=3,
                                    corner_radius=50, bg_color="transparent",
                                    text_color=color_yel,
                                    radiobutton_height=20,
                                    radiobutton_width=45,
                                    border_width_checked=3,
                                    border_color="black",
                                    border_width_unchecked=3,
                                    fg_color="yellow",
                                    hover_color="green",
                                    hover=True,
                                    font=("Calibri", 16)
                                    )
        FastMode2.place(x=400, y=160)
        
        FastMode3 = t.CTkRadioButton(master_under,text="𝗙𝗮𝘀𝘁 𝗠𝗼𝗱𝗲 𝗜𝗜𝗜", command=ChoseMode, variable=RadioVar, value=4,
                                    corner_radius=50, bg_color="transparent",
                                    text_color=color_yel,
                                    radiobutton_height=20,
                                    radiobutton_width=45,
                                    border_width_checked=3,
                                    border_color="black",
                                    border_width_unchecked=3,
                                    fg_color="yellow",
                                    hover_color="green",
                                    hover=True,
                                    font=("Calibri", 16)
                                    )
        FastMode3.place(x=400, y=200)
        
        
        
        SaveDataButton = t.CTkButton(master_under, text="Save Data Section",
                                    text_color="red",
                                    bg_color="transparent",
                                    border_color="darkblue",
                                    border_spacing=3,
                                    border_width=4,
                                    fg_color="blue",
                                    corner_radius=40,
                                    command=DataScreen,
                                    )
        SaveDataButton.place(x=776.5,y=5)


        QuitterL = t.CTkLabel(master_under,text="𝓠𝓾𝓲𝓽𝓽𝓮𝓻", text_color="black", fg_color="#393cff", bg_color="transparent", corner_radius=20, font=("Calibri", 24),width=100,height=16)  
        QuitterL.place(x=548, y=5)

        switchQuitter =t.CTkSwitch(master_under,switch_width=45,
                        text="OFF/ON",
                        text_color="#4ca6ae",
                        bg_color="transparent",
                        fg_color="#4051da",
                        border_color="blue", 
                        border_width=2,
                        button_color="#66b5ce",
                        button_hover_color="#284852",
                        progress_color="#33355e",
                        command=quitterSWITCH
                        )
        switchQuitter.place(x=550,y=40)

        RadioVar2 = t.StringVar(master_under)

        Quitter5 = t.CTkRadioButton(master_under,text="𝐕 𝑴𝒊𝒏", command=lambda: setMinutes(5), variable=RadioVar2, value=0,
                                    corner_radius=50, bg_color="transparent",
                                    text_color=color_yel,
                                    radiobutton_height=20,
                                    radiobutton_width=45,
                                    border_width_checked=3,
                                    border_color="black",
                                    border_width_unchecked=3,
                                    fg_color="#006f62",
                                    hover_color="#66a8a0",
                                    hover=True,
                                    font=("Calibri", 16)
                                    )
        Quitter5.place(x=550,y=80)

        Quitter10 = t.CTkRadioButton(master_under,text="𝐗 𝑴𝒊𝒏", command=lambda: setMinutes(10), variable=RadioVar2, value=1,
                                    corner_radius=50, bg_color="transparent",
                                    text_color=color_yel,
                                    radiobutton_height=20,
                                    radiobutton_width=45,
                                    border_width_checked=3,
                                    border_color="black",
                                    border_width_unchecked=3,
                                    fg_color="#006f62",
                                    hover_color="#66a8a0",
                                    hover=True,
                                    font=("Calibri", 16)
                                    )
        Quitter10.place(x=550,y=120)
        
        Quitter15 = t.CTkRadioButton(master_under,text="𝐗𝐕 𝑴𝒊𝒏", command=lambda: setMinutes(15), variable=RadioVar2, value=2,
                                    corner_radius=50, bg_color="transparent",
                                    text_color=color_yel,
                                    radiobutton_height=20,
                                    radiobutton_width=45,
                                    border_width_checked=3,
                                    border_color="black",
                                    border_width_unchecked=3,
                                    fg_color="#006f62",
                                    hover_color="#66a8a0",
                                    hover=True,
                                    font=("Calibri", 16)
                                    )
        Quitter15.place(x=550,y=160)
        
        Quitter20 = t.CTkRadioButton(master_under,text="𝐗𝐗 𝑴𝒊𝒏", command=lambda: setMinutes(20), variable=RadioVar2, value=3,
                                    corner_radius=50, bg_color="transparent",
                                    text_color=color_yel,
                                    radiobutton_height=20,
                                    radiobutton_width=45,
                                    border_width_checked=3,
                                    border_color="black",
                                    border_width_unchecked=3,
                                    fg_color="#006f62",
                                    hover_color="#66a8a0",
                                    hover=True,
                                    font=("Calibri", 16)
                                    )
        Quitter20.place(x=550,y=200)

        #--------------------------------------------------------------------------------------------------------------------------------------------------------
        master_exec = tabs.tab("AR_Executor")
        
        FrameKrnl = t.CTkFrame(master_exec, width=230,height=230, bg_color="transparent", fg_color="#ff71c2", border_color="#444449", border_width=10,corner_radius=20)
        FrameKrnl.place(x=5,y=5)
        
        krnlL = t.CTkLabel(FrameKrnl, text="Kʀɴʟ", font=("Calibri",27), bg_color="transparent", fg_color="transparent",text_color="#3b0e15")
        krnlL.place(x=85,y=10)
        
        krnlSwitch =t.CTkSwitch(FrameKrnl,switch_width=45,
                        text="OFF/ON",
                        text_color="#3e5c1d",
                        bg_color="transparent",
                        fg_color="#6a854d",
                        border_color="#d9e0d2", 
                        border_width=2,
                        button_color="#223310",
                        button_hover_color="#141e09",
                        progress_color="#060a03",
                        command=executorON_OFFKRNL)
        krnlSwitch.place(x=85,y=40)
        
        
        labelfors1 = t.CTkLabel(FrameKrnl, text="Insert Path And Submit:", text_color="black", bg_color="transparent", fg_color="transparent", font=("Calibri", 15))
        labelfors1.place(x=20,y=70)
        
        entryPath = t.CTkEntry(FrameKrnl, bg_color="transparent", corner_radius=20, fg_color="#314a76", border_color="#ffc6eb",border_width=2,text_color="#ffde01",width=180,height=32)
        entryPath.place(x=28,y=100)
        
        load_path_krnl = t.CTkButton(FrameKrnl, text="Loaded Path", corner_radius=20, fg_color="#3e3e42",bg_color="transparent", border_color="#0c0c0d",border_width=2,text_color="red",command=lambda:load_path_data("krnl"))
        load_path_krnl.place(x=45,y=140)
        
        submit1 = t.CTkButton(FrameKrnl, corner_radius=20,bg_color="transparent", 
                             fg_color="#10603e", text="Insert Path", text_color="#d1ece0",
                             border_color="green", border_width=2,hover_color="#052014",
                             command=submitKP)
        submit1.place(x=45,y=170)
        
        
        
        FrameFluxus = t.CTkFrame(master_exec, width=230,height=230, bg_color="transparent", fg_color="#a24c10", border_color="#008877", border_width=10,corner_radius=20)
        FrameFluxus.place(x=733,y=5)
        
        FluxusL = t.CTkLabel(FrameFluxus, text="Fʟᴜxᴜs", font=("Calibri",27), bg_color="transparent", fg_color="transparent",text_color="#3b0e15")
        FluxusL.place(x=75,y=10)
        
        FluxusSwitch =t.CTkSwitch(FrameFluxus,switch_width=45,
                        text="OFF/ON",
                        text_color="#4e262c",
                        bg_color="transparent",
                        fg_color="#350c12",
                        border_color="#362204", 
                        border_width=2,
                        button_color="#ff001a",
                        button_hover_color="#66000a",
                        progress_color="#190002",
                        command=executorON_OFFFLUXUS)
        FluxusSwitch.place(x=85,y=40)
        
        
        labelfors2 = t.CTkLabel(FrameFluxus, text="Insert Path And Submit:", text_color="black", bg_color="transparent", fg_color="transparent", font=("Calibri", 15))
        labelfors2.place(x=20,y=70)
        
        
        entryPath2 = t.CTkEntry(FrameFluxus, bg_color="transparent", corner_radius=20, fg_color="#314a76", border_color="#ffc6eb",border_width=2,text_color="#ffde01",width=180,height=32)
        
        entryPath2.place(x=28,y=100)
        
        load_path_flux = t.CTkButton(FrameFluxus, text="Loaded Path", corner_radius=20, fg_color="#3e3e42",bg_color="transparent", border_color="#0c0c0d",border_width=2,text_color="red",command=lambda:load_path_data("flux"))
        load_path_flux.place(x=45,y=140)
        
        submit2 = t.CTkButton(FrameFluxus, corner_radius=20,bg_color="transparent", 
                             fg_color="#10603e", text="Insert Path", text_color="#d1ece0", border_color="green", 
                             border_width=2,hover_color="#052014",
                             command=submitKP)
        submit2.place(x=45,y=170)
        
        labeltosay = t.CTkLabel(master_exec, text="Insert The Path To Save:", text_color="yellow", bg_color="transparent", fg_color="transparent",font=("Calibri", 18))
        labeltosay.place(x=310,y=15)
        
        entrySave= t.CTkEntry(master_exec, text_color="yellow", border_color="yellow", border_width=2,bg_color="transparent", fg_color="transparent",corner_radius=20, width=200,height=34)
        entrySave.place(x=380,y=50)
        
        krnlsaveB = t.CTkButton(master_exec, text_color="pink", border_color="#d793e8", border_width=2, bg_color="transparent", fg_color="#000e18",text="Save Krnl Path",command=lambda: store_paths_ex("KRNL"))
        fluxussaveB =t.CTkButton(master_exec, text_color="pink", border_color="#d793e8", border_width=2, bg_color="transparent", fg_color="#000e18",text="Save Fluxus Path",command=lambda: store_paths_ex("FLUXUS"))
        
        krnlsaveB.place(x=270,y=100)
        fluxussaveB.place(x=550,y=100)
        
        #--------------------------------------------------------------------------------------------------------------------------------------------------------
        master_theme = tabs.tab("ThemeSW")
        
        Welcome_Theme = t.CTkLabel(master_theme, text="𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑰𝒏 𝑻𝒉𝒆𝒎𝒆𝒔",font=("Calibri", 40),text_color="#f3c2a1",bg_color="transparent", fg_color="transparent")
        Welcome_Theme.place(x=300,y=0)
        
        FrameOne = t.CTkFrame(master_theme,bg_color="transparent", fg_color="#4ca6a6",corner_radius=20, border_color="#b2d8d8",border_width=3,width=180,height=180)
        FrameOne.place(x=8,y=50)
        
        FrameTwo = t.CTkFrame(master_theme,bg_color="transparent", fg_color="#23235c",corner_radius=20, border_color="#b2d8d8",border_width=3,width=180,height=180)
        FrameTwo.place(x=198,y=50)
        
        FrameThree = t.CTkFrame(master_theme,bg_color="transparent", fg_color="#a24c10",corner_radius=20, border_color="#b2d8d8",border_width=3,width=180,height=180)
        FrameThree.place(x=388,y=50)
        
        FrameFour = t.CTkFrame(master_theme,bg_color="transparent", fg_color="#ff001a",corner_radius=20, border_color="#b2d8d8",border_width=3,width=180,height=180)
        FrameFour.place(x=578,y=50)
        
        FrameFive = t.CTkFrame(master_theme,bg_color="transparent", fg_color="#ff80ed",corner_radius=20, border_color="#b2d8d8",border_width=3,width=180,height=180)
        FrameFive.place(x=768,y=50)
        
        #FRAME ONE
        Fg_section = t.CTkLabel(FrameOne, text="𝑭𝒐𝒓𝒆𝒈𝒓𝒐𝒖𝒏𝒅 𝑪𝒐𝒍𝒐𝒓", text_color="#b2d8d8",bg_color="transparent", fg_color="transparent",font=("calibri", 18))
        Fg_section.place(x=20,y=15)
        
        colors_fg = []
        
        StringColorOne = t.StringVar(value=colors_fg)
        color_text = "#340000"
        border_color= "#094873"
        fg_colors = "#073656"
        hover_co = "#02121c"
        
        color_fg1 = t.CTkRadioButton(FrameOne, variable=StringColorOne, value=1,
                                    corner_radius=30, bg_color="transparent",
                                    text_color=color_text,
                                    radiobutton_height=20,
                                    radiobutton_width=70,
                                    border_width_checked=3,
                                    border_color=border_color,
                                    border_width_unchecked=3,
                                    fg_color=fg_colors,
                                    hover_color=hover_co,
                                    hover=True,
                                    font=("Calibri", 16),
                                    text="Dᴇᴀғᴜʟᴛ",
                                    command=lambda:default_fg_color())
        color_fg1.place(x=10,y=50)
        
        color_fg2 = t.CTkRadioButton(FrameOne, variable=StringColorOne, value=1,
                                    corner_radius=30, bg_color="transparent",
                                    text_color=color_text,
                                    radiobutton_height=20,
                                    radiobutton_width=70,
                                    border_width_checked=3,
                                    border_color=border_color,
                                    border_width_unchecked=3,
                                    fg_color=fg_colors,
                                    hover_color=hover_co,
                                    hover=True,
                                    font=("Calibri", 16),
                                    text="Tʜᴇᴍᴇ F1",
                                    command=lambda:fg_color_set("red"))
        color_fg2.place(x=10,y=90)
        
        color_fg3 = t.CTkRadioButton(FrameOne, variable=StringColorOne, value=1,
                                    corner_radius=30, bg_color="transparent",
                                    text_color=color_text,
                                    radiobutton_height=20,
                                    radiobutton_width=70,
                                    border_width_checked=3,
                                    border_color=border_color,
                                    border_width_unchecked=3,
                                    fg_color=fg_colors,
                                    hover_color=hover_co,
                                    hover=True,
                                    font=("Calibri", 16),
                                    text="Tʜᴇᴍᴇ F2",
                                    command=lambda:fg_color_set("darkblue"))
        color_fg3.place(x=10,y=130)
        
        #FRAME TWO
        Fg_section = t.CTkLabel(FrameTwo, text="𝑩𝒂𝒄𝒌𝒈𝒓𝒐𝒖𝒏𝒅 𝑪𝒐𝒍𝒐𝒓", text_color="#0047bb",bg_color="transparent", fg_color="transparent",font=("calibri", 18))
        Fg_section.place(x=20,y=15)
        
        colors_fg = []
        
        StringColorOne = t.StringVar(value=colors_fg)
        color_text = "#008877"
        border_color= "#510212"
        fg_colors = "#115511"
        hover_co = "#031103"
        
        color_bg1 = t.CTkRadioButton(FrameTwo, variable=StringColorOne, value=1,
                                    corner_radius=30, bg_color="transparent",
                                    text_color=color_text,
                                    radiobutton_height=20,
                                    radiobutton_width=70,
                                    border_width_checked=3,
                                    border_color=border_color,
                                    border_width_unchecked=3,
                                    fg_color=fg_colors,
                                    hover_color=hover_co,
                                    hover=True,
                                    font=("Calibri", 16),
                                    text="Dᴇᴀғᴜʟᴛ",
                                    command=lambda:default_bg_color())
        color_bg1.place(x=10,y=50)
        
        color_bg2 = t.CTkRadioButton(FrameTwo, variable=StringColorOne, value=1,
                                    corner_radius=30, bg_color="transparent",
                                    text_color=color_text,
                                    radiobutton_height=20,
                                    radiobutton_width=70,
                                    border_width_checked=3,
                                    border_color=border_color,
                                    border_width_unchecked=3,
                                    fg_color=fg_colors,
                                    hover_color=hover_co,
                                    hover=True,
                                    font=("Calibri", 16),
                                    text="Tʜᴇᴍᴇ F1",
                                    command=lambda:bg_color_set("red"))
        color_bg2.place(x=10,y=90)
        
        color_bg3 = t.CTkRadioButton(FrameTwo, variable=StringColorOne, value=1,
                                    corner_radius=30, bg_color="transparent",
                                    text_color=color_text,
                                    radiobutton_height=20,
                                    radiobutton_width=70,
                                    border_width_checked=3,
                                    border_color=border_color,
                                    border_width_unchecked=3,
                                    fg_color=fg_colors,
                                    hover_color=hover_co,
                                    hover=True,
                                    font=("Calibri", 16),
                                    text="Tʜᴇᴍᴇ F2",
                                    command=lambda:bg_color_set("darkblue"))
        color_bg3.place(x=10,y=130)
        
        #FRAME THREE
        Fg_section = t.CTkLabel(FrameThree, text="𝙁𝙜 𝘾𝙤𝙡𝙤𝙧 𝙍𝙚𝙡𝙤𝙖𝙙𝙚𝙧𝙎𝙒", text_color="#b46f3f",bg_color="transparent", fg_color="transparent",font=("calibri", 18))
        Fg_section.place(x=20,y=15)
        
        colors_fg = []
        
        StringColorOne = t.StringVar(value=colors_fg)
        color_text = "#d0a587"
        border_color= "#100701"
        fg_colors = "#eeaa7c"
        hover_co = "#452814"
        
        color_bg1 = t.CTkRadioButton(FrameThree, variable=StringColorOne, value=1,
                                    corner_radius=30, bg_color="transparent",
                                    text_color=color_text,
                                    radiobutton_height=20,
                                    radiobutton_width=70,
                                    border_width_checked=3,
                                    border_color=border_color,
                                    border_width_unchecked=3,
                                    fg_color=fg_colors,
                                    hover_color=hover_co,
                                    hover=True,
                                    font=("Calibri", 16),
                                    text="Dᴇᴀғᴜʟᴛ",
                                    command=lambda:default_fg_Main_color())
        color_bg1.place(x=10,y=50)
        
        color_bg2 = t.CTkRadioButton(FrameThree, variable=StringColorOne, value=1,
                                    corner_radius=30, bg_color="transparent",
                                    text_color=color_text,
                                    radiobutton_height=20,
                                    radiobutton_width=70,
                                    border_width_checked=3,
                                    border_color=border_color,
                                    border_width_unchecked=3,
                                    fg_color=fg_colors,
                                    hover_color=hover_co,
                                    hover=True,
                                    font=("Calibri", 16),
                                    text="Tʜᴇᴍᴇ F1",
                                    command=lambda:fg_Main_color_set("red"))
        color_bg2.place(x=10,y=90)
        
        color_bg3 = t.CTkRadioButton(FrameThree, variable=StringColorOne, value=1,
                                    corner_radius=30, bg_color="transparent",
                                    text_color=color_text,
                                    radiobutton_height=20,
                                    radiobutton_width=70,
                                    border_width_checked=3,
                                    border_color=border_color,
                                    border_width_unchecked=3,
                                    fg_color=fg_colors,
                                    hover_color=hover_co,
                                    hover=True,
                                    font=("Calibri", 16),
                                    text="Tʜᴇᴍᴇ F2",
                                    command=lambda:fg_Main_color_set("darkblue"))
        color_bg3.place(x=10,y=130)
        
        #FRAME FOUR
        Fg_section = t.CTkLabel(FrameFour, text="𝙁𝙜 𝘾𝙤𝙡𝙤𝙧 𝘼𝙍_𝙀𝙭𝙚𝙘𝙪𝙩𝙤𝙧", text_color="#751818",bg_color="transparent", fg_color="transparent",font=("calibri", 18))
        Fg_section.place(x=20,y=15)
        
        colors_fg = []
        
        StringColorOne = t.StringVar(value=colors_fg)
        color_text = "#771919"
        border_color= "#680000"
        fg_colors = "#a46666"
        hover_co = "#0a0000"
        
        color_bg1 = t.CTkRadioButton(FrameFour, variable=StringColorOne, value=1,
                                    corner_radius=30, bg_color="transparent",
                                    text_color=color_text,
                                    radiobutton_height=20,
                                    radiobutton_width=70,
                                    border_width_checked=3,
                                    border_color=border_color,
                                    border_width_unchecked=3,
                                    fg_color=fg_colors,
                                    hover_color=hover_co,
                                    hover=True,
                                    font=("Calibri", 16),
                                    text="Dᴇᴀғᴜʟᴛ",
                                    command=lambda:default_fg_ExecSW_color())
        color_bg1.place(x=10,y=50)
        
        color_bg2 = t.CTkRadioButton(FrameFour, variable=StringColorOne, value=1,
                                    corner_radius=30, bg_color="transparent",
                                    text_color=color_text,
                                    radiobutton_height=20,
                                    radiobutton_width=70,
                                    border_width_checked=3,
                                    border_color=border_color,
                                    border_width_unchecked=3,
                                    fg_color=fg_colors,
                                    hover_color=hover_co,
                                    hover=True,
                                    font=("Calibri", 16),
                                    text="Tʜᴇᴍᴇ F1",
                                    command=lambda:fg_ExecSW_color_set("red"))
        color_bg2.place(x=10,y=90)
        
        color_bg3 = t.CTkRadioButton(FrameFour, variable=StringColorOne, value=1,
                                    corner_radius=30, bg_color="transparent",
                                    text_color=color_text,
                                    radiobutton_height=20,
                                    radiobutton_width=70,
                                    border_width_checked=3,
                                    border_color=border_color,
                                    border_width_unchecked=3,
                                    fg_color=fg_colors,
                                    hover_color=hover_co,
                                    hover=True,
                                    font=("Calibri", 16),
                                    text="Tʜᴇᴍᴇ F2",
                                    command=lambda:fg_ExecSW_color_set("darkblue"))
        color_bg3.place(x=10,y=130)
        
        #FRAME FIVE
        Fg_section = t.CTkLabel(FrameFive, text="𝙁𝙜 𝘾𝙤𝙡𝙤𝙧 𝙏𝙝𝙚𝙢𝙚𝙎𝙒", text_color="#ffffff",bg_color="transparent", fg_color="transparent",font=("calibri", 18))
        Fg_section.place(x=20,y=15)
        
        colors_fg = []
        
        StringColorOne = t.StringVar(value=colors_fg)
        color_text = "#63336f"
        border_color= "#ffb2f4"
        fg_colors = "#7f4076"
        hover_co = "#33192f"
        
        color_bg1 = t.CTkRadioButton(FrameFive, variable=StringColorOne, value=1,
                                    corner_radius=30, bg_color="transparent",
                                    text_color=color_text,
                                    radiobutton_height=20,
                                    radiobutton_width=70,
                                    border_width_checked=3,
                                    border_color=border_color,
                                    border_width_unchecked=3,
                                    fg_color=fg_colors,
                                    hover_color=hover_co,
                                    hover=True,
                                    font=("Calibri", 16),
                                    text="Dᴇᴀғᴜʟᴛ",
                                    command=lambda:default_fg_Theme_color())
        color_bg1.place(x=10,y=50)
        
        color_bg2 = t.CTkRadioButton(FrameFive, variable=StringColorOne, value=1,
                                    corner_radius=30, bg_color="transparent",
                                    text_color=color_text,
                                    radiobutton_height=20,
                                    radiobutton_width=70,
                                    border_width_checked=3,
                                    border_color=border_color,
                                    border_width_unchecked=3,
                                    fg_color=fg_colors,
                                    hover_color=hover_co,
                                    hover=True,
                                    font=("Calibri", 16),
                                    text="Tʜᴇᴍᴇ F1",
                                    command=lambda:fg_Theme_color_set("red"))
        color_bg2.place(x=10,y=90)
        
        color_bg3 = t.CTkRadioButton(FrameFive, variable=StringColorOne, value=1,
                                    corner_radius=30, bg_color="transparent",
                                    text_color=color_text,
                                    radiobutton_height=20,
                                    radiobutton_width=70,
                                    border_width_checked=3,
                                    border_color=border_color,
                                    border_width_unchecked=3,
                                    fg_color=fg_colors,
                                    hover_color=hover_co,
                                    hover=True,
                                    font=("Calibri", 16),
                                    text="Tʜᴇᴍᴇ F2",
                                    command=lambda:fg_Theme_color_set("darkblue"))
        color_bg3.place(x=10,y=130)
        
        
        
        #MAIN#
        MainReSC = schedule.Scheduler()
        MainReSC.every(VELOCITY_REJOIN).seconds.do(upd_status)
        
        #QUITTER SC#
        quitterSC = schedule.Scheduler()
        quitterSC.every(MINUTES).minutes.do(FORCEapple)
        
        #EXECUTORS
        FluxusSC = schedule.Scheduler()
        FluxusSC.every(15).minutes.do(executor_rejoinedFLUXUS)

        KrnlSC = schedule.Scheduler()
        KrnlSC.every(15).minutes.do(executor_rejoinedKRNL)
        
        
        #HERE WHILE#
        while ONLINE:
            window.update()
            
            MainReSC.run_pending()
            quitterSC.run_pending()
            FluxusSC.run_pending()
            KrnlSC.run_pending()
