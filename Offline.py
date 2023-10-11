

if OFFLINE:
        def offdef():
            try:
                offL.destroy()
                os.system(f'taskkill /f /im   {os.getpid()}')
                sys.exit()
            except:pass

        offL = t.CTk()
        offL.title("𝔸𝕦𝕥𝕠ℝ𝕖𝕝𝕠𝕒𝕕𝕖𝕣 𝕆𝕗𝕗𝕝𝕚𝕟𝕖")
        offL.geometry("320x460")
        offL._set_appearance_mode("dark")
        offL.resizable(False,False)
        offL.protocol("WM_DELETE_WINDOW", offdef)

        appleRaw = res_path("apple.ico")

        als = "mycompany.myproduct.subproduct.version"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(als)
        offL.iconbitmap(appleRaw)
        backgroundxD = t.CTkFrame(offL, bg_color="purple", fg_color="green",corner_radius=20,border_color="blue", border_width=3)
        backgroundxD.pack(fill="both", expand=1)
        
        OFFLAB = t.CTkLabel(backgroundxD, text="AutoReloaderSW Is Offline\n\nFor More Info ↓↓↓",font=("Calibri", 20),text_color="yellow",)
        OFFLAB.place(x=50,y=20)
        
        discordbutton = t.CTkButton(backgroundxD, text="Join Discord", bg_color="transparent", fg_color="blue",width=110 ,hover_color="darkblue",corner_radius=20,command=lambda:webbrowser.open("https://discord.gg/qrqc6jcKRW", autoraise=True))        
        discordbutton.place(x=160, y=90)


        offL.mainloop()
