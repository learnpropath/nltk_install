::In Terminal Check Python is installed or not 
    :~<path>$ python3 --version

::Create a dir nltk_install and cd to nltk_install 

::Create a virturalenv 'nltk_venv'
    :~<path>$ python3 -m venv nltk_venv

    || if the above command error, install virtualenv using 'sudo apt install python3.12-venv' and retry the above code.

::Validate the env is created in the folder
    :~<path>$ ls -ltr

::Activate the nltk_venv environment
    :~<path>$ . nltk_venv/bin/activate

::Deactivte the environment 
    :~<path>$ deactivate 

|---0---0---0---0---0---|
Start VSCode:

1. Inside VSCode open a termina windows

2. In vscode terminal, type . nltk_venv/bin/activate

3. run 'pip install nltk' 

3a. run 'pip install scikit-learn'

4. to confirm run'pip list'

5. Confirm 'python' has the visibility to nltk lib
    
    run python3 
    in python prompt 
        >>> import ntlk
        >>> ntlk.__version__   ... this should output the version '3.9.1'
        >>> exit()  ... to get out of python shell

4. Create a file test.py with the following code
        import nltk
        print(nltk.__version__)
    run the above file in vscode and you should get the output of the version '3.9.1'

5. Install the nltk dependent packages 
        create a 1.py with code as follows:
            import nltk
            nltk.download()
        run the above 1.py code in VSCode IDE and this should pop-up a ntlk downloader
            (... be patient, it may take some time)

        Alternatively you can also run this 1.py in the YSCode termina by this:
            python 1.py

        
|---0---0---0---0---|
Resources: 

    This project could not be completed without these refered resources 

    YT Video || Joey'sTech || How to Install NLTK in Python 3 in less than 5 mins - a step by step process #python || https://www.youtube.com/watch?v=85Xr0UGR8qQ

    YT Video || Python NLTK Tutorial 1 - Getting started with NLTK || ProgrammingKnowledge || https://www.youtube.com/watch?v=LQQbW3Pve5U
