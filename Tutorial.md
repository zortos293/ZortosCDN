## Adding a New App:

1. Click on the "Add App" button in the "Add New App" section.
2. Fill in the following details for the app:
- **Name**: Enter the name of the app.
- **URL**: Provide a link to the app's website or download page.
- **Zip**: If the app is provided as a ZIP file, enable this option. Otherwise, leave it unchecked.
- **Launch Path**: Specify the relative path to the app's executable file within the ZIP folder (if applicable) or the standalone executable file. For example, if the executable is in a folder named "App" and the executable file is "app.exe," the launch path should be "App/app.exe."


## Editing an App:

To edit an app's details, click the "Edit" button next to the app you want to modify.
Update the app's name, URL, zip option, or launch path as needed.
Click the "Save" button to save your changes or the "Cancel" button to discard them.


## Viewing App Details:

In the Apps list, you can view the details of each added app, including the app's name, URL, whether it's a ZIP, and the launch path.
You can also edit any app by clicking the "Edit" button.


## Saving and Copying JSON Configuration:

You can click the "Copy JSON" button to generate the updated JSON configuration for your CloudOS.
The JSON will include the details of all the apps you've added, along with the wallpaper URL and style.

## Changing Wallpaper:

You can change the wallpaper URL by entering a new URL in the "Wallpaper URL" input field. Make sure to use a valid image URL.


## Paste JSON from Clipboard:

You can paste JSON from the clipboard using the "Paste JSON from Clipboard" button. This allows you to quickly import a previously saved configuration.


## Final Configuration Example:

Here's an example of what your final JSON configuration might look like:


```json
{
  "wallpaperURL": "https://your-wallpaper-image-url.com/image.jpg",
  "wallpaperStyle": "fill",
  "apps": [
    {
      "name": "App 1",
      "url": "https://example.com/app1",
      "zip": false,
      "launchPath": ""
    },
    {
      "name": "App 2",
      "url": "https://example.com/app2.zip",
      "zip": true,
      "launchPath": "App2/app2.exe"
    },
    // Add more apps as needed
  ]
}
```

That's it! You can follow these steps to add and manage apps in your CloudOS Preset. Be sure to provide accurate URLs and launch paths for the apps you want to include.



## Copying JSON Configuration:

As mentioned earlier, click the "Copy JSON" button to generate your updated JSON configuration, including all the apps and wallpaper settings.

## Uploading JSON to Pastebin:

- Open your web browser and go to Pastebin.

- If you don't already have an account, consider signing up for a free Pastebin account. It's not required, but having an account can be useful for managing your pastes.
- Click the "New Paste" button on the Pastebin homepage.

- Paste the copied JSON configuration into the text box provided.

- Optionally, you can choose the expiration date for your paste, set a paste name/title, and select a privacy setting (Public).

- Click the "Create Paste" button.


- After creating the paste, you'll be redirected to the paste's unique URL. It will look something like this: https://pastebin.com/your-paste-id.

## Getting the Raw JSON Link:

- To get the raw JSON link, click on the "Raw" button on the top-right corner of the paste page. This will display only the raw JSON content without any Pastebin formatting.

- Copy the URL from your browser's address bar. This is the raw JSON link that you'll use to import into CloudOSGFN.

## Running your custom Preset

- run CloudOS 
- you will see two options default CloudOS and Custom
- Select custom using keyboard arrow then press enter
- paste your raw pastebin link and press enter
- if its correct it will now download your apps and apply your background

