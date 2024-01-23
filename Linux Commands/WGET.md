`wget` is a powerful command-line utility for downloading files from the web. It supports various protocols such as HTTP, HTTPS, FTP, and FTPS. 

1.**Basic File Download**

This command downloads the file named `file.zip` from the specified URL.

```bash
wget https://example.com/file.zip
```

Example: 
```bash
wget https://sample-videos.com/zip/10mb.zip
```

![[Pasted image 20240120220101.png]]

2.**Download to a specific directory**

```bash
wget -P /path/to/directory https://example.com/file.zip
```

Example:
```bash
wget -P Downloads https://sample-videos.com/zip/10mb.zip
```

![[Pasted image 20240120220525.png]]

3.**Download with a different name**

```bash
wget -O newname.zip https://example.com/file.zip
```

Downloads the file and save it as newname.zip

Example:
```bash
wget -O newname.zip  https://sample-videos.com/zip/10mb.zip
```

![[Pasted image 20240120220835.png]]

4.**Download multiple files**

```bash
wget https://example.com/file1.zip https://example.com/file2.zip
```

Example:

```bash
wget https://sample-videos.com/zip/10mb.zip https://sample-videos.com/zip/20mb.zip
```

![[Pasted image 20240120221130.png]]

5.**Download in Background**

```bash
wget -b https://example.com/largefile.zip
```

Example:
```bash
wget -b -O 20mnbfile.zip https://sample-videos.com/zip/20mb.zip
```

![[Pasted image 20240120221501.png]]

It will write the logs in to wget-log txt file. 
6.**Rate Limiting Download**

```bash
wget --limit-rate=200k https://example.com/largefile.zip
```

it limits the download rate to 200 Kb/s.

Example:
```bash
wget --limit-rate=200k https://sample-videos.com/zip/20mb.zip
```

![[Pasted image 20240121070528.png]]
7.**Resume Interrupted Download**
```bash
wget -c https://example.com/largefile.zip
```

Example:
```bash
wget --limit-rate=200k https://sample-videos.com/zip/20mb.zip
```

![[Pasted image 20240121071141.png]]

8.**Downloading Entire Website**
```bash
wget --recursive --no-clobber --page-requisites --html-extension --convert-links --domains example.com --no-parent https://example.com

```

- **`--recursive`**: Enables recursive retrieval, meaning `wget` will download not only the specified URL but also follow and download links within that page, continuing recursively.
    
- **`--no-clobber`**: This option prevents `wget` from overwriting existing files. If a file with the same name already exists in the local directory, `wget` will not download it again.
    
- **`--page-requisites`**: Downloads all the elements needed to properly display the page offline. This includes inline images, stylesheets, and other resources referenced by the HTML.
    
- **`--html-extension`**: Appends the `.html` extension to HTML files downloaded. This is useful when saving a complete website for offline browsing, as it helps maintain proper file extensions.
    
- **`--convert-links`**: After downloading, converts the links in the downloaded documents to point to the local files, enabling offline browsing. This is important when you want to view the downloaded content without an internet connection.
    
- **`--domains example.com`**: Restricts the download to files under the specified domain (`example.com`). This ensures that `wget` doesn't follow links to external domains, focusing only on the specified domain.
    
- **`--no-parent`**: Prevents `wget` from ascending to the parent directory while recursively downloading. It ensures that only content within the specified URL and its subdirectories is downloaded.
    
- **`https://example.com`**: The URL from which `wget` starts the recursive download.

Example:
```bash
wget --recursive --no-clobber --page-requisites --html-extension --convert-links --domains hashnode.dev --no-parent https://redterminal.hashnode.dev

```
![[Pasted image 20240121071805.png]]

9.**Mirror an entire website**
```bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://example.com

```

- **`--mirror`**: Enables mirroring, which includes recursion to download the entire website.
- **`--convert-links`**: Converts the links in the downloaded documents to point to the local files for proper offline browsing.
- **`--adjust-extension`**: Adds proper file extensions to downloaded files.
- **`--page-requisites`**: Downloads all the elements needed to properly display the page offline, such as inline images and stylesheets.
- **`--no-parent`**: Prevents `wget` from ascending to the parent directory while recursively downloading.

Example:
```bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://example.com
```
![[Pasted image 20240121071918.png]]
10.**Download with a user-agent**

Some websites block the request, if it finds the request is not coming from a browser. In those scenarios we can add the User-Agent in the http-header. 

```bash
wget --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3" https://example.com/file.zip
```

Example:

```bash
wget --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3" https://sample-videos.com/zip/20mb.zip

```

![[Pasted image 20240121072245.png]]

11.**Download with proxy** - [[Proxy Server]]

```bash
wget --proxy=http://proxy.example.com:8080 https://example.com/file.zip
```

12.**Download files matching a pattern**

```bash
wget -r -l1 -np -nd -A "*.jpg" https://example.com/images/
```

- l1 -> Recursion depth level 1
- np -> No parent directory files downloaded
- nd -> No directory created

13.**Test download url exists before downloading**
```bash
wget --spider https://example.com
```

Example:
```bash
wget --spider https://sample-videos.com/zip/10mb.zip
```

If the file exists, 
![[Pasted image 20240121074049.png]]

If the file is not present, 
![[Pasted image 20240121074119.png]]

14.**Quit Download when it exceeds a certain time**
```bash
wget -Q5m -i FILE-WHICH-HAS-URLS
```

Example:
```bash
wget -Q5m -i https://sample-videos.com/zip/10mb.zip https://sample-videos.com/zip/20mb.zip
```

![[Pasted image 20240121074619.png]]

**Note:** This quota will not get effect when you do a download a single URL. That is irrespective of the quota size everything will get downloaded when you specify a single file. This quota is applicable only for recursive downloads.

Lets try with recursive download,

```bash
wget --recursive -Q5m --no-clobber --page-requisites --html-extension --convert-links --domains hashnode.dev --no-parent https://redterminal.hashnode.dev
```

![[Pasted image 20240121074833.png]]

15.**Increase total number of retries**
```bash
wget --tries=75 DOWNLOAD-URL
```

