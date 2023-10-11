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
