# beryllium-makelogo
Create your own version of logo.img for beryllium (Xiaomi POCO F1) on MIUI 12!

# Why use this instead of pocosplasher?
If you are using MIUI 12.0.0 and higher on your POCO F1, you might have noticed that the boot logo changed.<br>
This also affected the layout of the logo.img file and pocosplasher never got updated. So, use this instead.

# Requirements
* POCO F1 (beryllium) DON'T TRY ON SURYA OR ANY OTHER POCO THAN BERYLLIUM
* Python 3 or higher
* MIUI 12 or higher (or custom ROM with the updated firmware)
* Unlocked bootloader

# How do I use this?
Download this repository to your computer. Edit the BMP files. Make sure you don't use any transparency or change the resolution. Also, export as a 24-bit BMP, not lower or higher.<br>
After your done, run the Python script and do ```fastboot flash logo /path/to/logo.img```. Restart the phone and your'e done!

# How do I restore the original?
I provided the original IMG file with the program, so do the same fastboot command but to the ORIGINAL.img file.
