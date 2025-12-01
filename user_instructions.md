It's now clear why both `npx` and `npm` commands are failing with the `PSSecurityException`. Both `npx` and `npm` are implemented as PowerShell scripts on your system, and your PowerShell execution policy is preventing them from running.

I cannot programmatically change your system's security settings from within this environment. To unblock this, you have two options:

**Option 1 (Recommended): Change your PowerShell Execution Policy (outside this session):**
Open a new PowerShell terminal (not within this environment) and run the following command:
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

This is a common and reasonably secure policy that allows scripts you create locally to run, while still requiring scripts downloaded from the internet to be signed by a trusted publisher. After running this, I should be able to execute `npx create-next-app`.

**Option 2 (Alternative): Manually run the command:**
Open a new terminal (either PowerShell or cmd.exe) in the project's root directory (`C:\Users\trioe\OneDrive\Trine\Molde 3.år\H IBE160 Programmering med KI\SG-Trine\`) and run the following command yourself:
`npx create-next-app@latest nextjs-frontend --typescript --eslint --app --src-dir --import-alias "@/*"`

Once you have successfully created the `nextjs-frontend` project, please let me know, and I can then proceed with creating the `api` backend and debugging the errors.