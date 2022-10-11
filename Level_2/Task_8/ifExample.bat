:: Checking if the new_folder exists
if EXIST new_folder (
    mkdir if_folder 
)

:: Checking if the if_folder exists
if EXIST if_folder (
    mkdir hyperionDev
) 
:: Else creating the react-projects folder.
else (
    mkdir react-projects
)