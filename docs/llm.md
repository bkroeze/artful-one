### Install LLM Tool

Source: https://github.com/simonw/llm/blob/main/docs/setup.md

Instructions for installing the LLM command-line tool using various package managers: pip, pipx, uv, and Homebrew.

```bash
pip install llm
```

```bash
pipx install llm
```

```bash
uv tool install llm
```

```bash
brew install llm
```

--------------------------------

### Install LLM Plugins

Source: https://github.com/simonw/llm/blob/main/docs/setup.md

Shows how to install LLM plugins, such as 'llm-gpt4all', to extend functionality and add support for additional language models, including those that can run locally.

```bash
llm install llm-gpt4all
```

--------------------------------

### Run LLM with uvx (Temporary Environment)

Source: https://github.com/simonw/llm/blob/main/docs/setup.md

Demonstrates how to use 'uvx' to run the LLM tool without a permanent installation, including setting API keys and adding extra plugins like 'llm-anthropic' for specific models.

```bash
export OPENAI_API_KEY='sx-...'
uvx llm 'fun facts about skunks'
```

```bash
export ANTHROPIC_API_KEY='...'
uvx --with llm-anthropic llm -m claude-3.5-haiku 'fun facts about skunks'
```

```bash
uvx llm keys set openai
```

--------------------------------

### Building Documentation Locally - Bash

Source: https://github.com/simonw/llm/blob/main/docs/contributing.md

Navigates to the 'docs' directory, installs documentation dependencies, and starts a live preview server for local documentation development. This uses Sphinx and sphinx-autobuild for real-time updates.

```bash
cd docs
pip install -r requirements.txt
make livehtml
```

--------------------------------

### Example Output of Listing LLM Plugins (JSON)

Source: https://github.com/simonw/llm/blob/main/docs/plugins/installing-plugins.md

This JSON snippet illustrates the typical output when running the llm plugins command. It shows an array of objects, each representing an installed plugin with its name, registered hooks, and version.

```json
[
  {
    "name": "llm-anthropic",
    "hooks": [
      "register_models"
    ],
    "version": "0.11"
  },
  {
    "name": "llm-gguf",
    "hooks": [
      "register_commands",
      "register_models"
    ],
    "version": "0.1a0"
  },
  {
    "name": "llm-clip",
    "hooks": [
      "register_commands",
      "register_embedding_models"
    ],
    "version": "0.1"
  },
  {
    "name": "llm-cmd",
    "hooks": [
      "register_commands"
    ],
    "version": "0.2a0"
  },
  {
    "name": "llm-gemini",
    "hooks": [
      "register_embedding_models",
      "register_models"
    ],
    "version": "0.3"
  }
]
```

--------------------------------

### Updating CLI Help Examples with Cog - Bash

Source: https://github.com/simonw/llm/blob/main/docs/contributing.md

Runs the 'just cog' command to update CLI `--help` examples in the documentation, which are managed using Cog. This command requires the 'Just' tool to be installed on the system.

```bash
just cog
```

--------------------------------

### Save and Use Stored LLM API Keys

Source: https://github.com/simonw/llm/blob/main/docs/setup.md

Explains how to save API keys using the 'llm keys set' command for automatic use in subsequent commands, how to list stored keys, and where the 'keys.json' file is located.

```bash
llm keys set openai
```

```bash
llm "Five ludicrous names for a pet lobster"
```

```bash
llm keys
```

```bash
llm keys path
```

--------------------------------

### Pass LLM API Keys via --key Option

Source: https://github.com/simonw/llm/blob/main/docs/setup.md

Demonstrates how to pass API keys directly using the '--key' option, either as a raw key string or by referencing an alias of a previously stored key.

```bash
llm "Five names for pet weasels" --key sk-my-key-goes-here
```

```bash
llm keys set personal
```

```bash
llm "Five friendly names for a pet skunk" --key personal
```

--------------------------------

### Upgrade LLM Tool

Source: https://github.com/simonw/llm/blob/main/docs/setup.md

Commands to upgrade the LLM tool to its latest version using pip, pipx, uv, or Homebrew. Includes a fallback method for Homebrew if the latest version isn't immediately available.

```bash
pip install -U llm
```

```bash
pipx upgrade llm
```

```bash
uv tool upgrade llm
```

```bash
brew upgrade llm
```

```bash
llm install -U llm
```

--------------------------------

### Use LLM API Keys from Environment Variables

Source: https://github.com/simonw/llm/blob/main/docs/setup.md

Describes how LLM can read API keys from environment variables (e.g., OPENAI_API_KEY) and how to explicitly use them with the '--key' option, prioritizing them over stored keys.

```bash
llm 'my prompt' --key $OPENAI_API_KEY
```

--------------------------------

### Workaround for PyTorch with Homebrew LLM

Source: https://github.com/simonw/llm/blob/main/docs/setup.md

Provides a workaround for installing PyTorch-dependent LLM plugins (e.g., 'llm-sentence-transformers') when using the Homebrew version of LLM, due to Python 3.12 compatibility issues with PyTorch.

```bash
llm install llm-python
llm python -m pip install \
  --pre torch torchvision \
  --index-url https://download.pytorch.org/whl/nightly/cpu
llm install llm-sentence-transformers
```

--------------------------------

### Install sqlite-utils for Database Operations

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

Instructions to install the `sqlite-utils` command-line tool, which is used for interacting with SQLite databases, via `uv tool install` or `pip`.

```bash
uv tool install sqlite-utils
# or pip install or pipx install
```

--------------------------------

### Verify LLM Plugin Installation

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Command to list all installed LLM plugins, confirming the presence of `llm-markov` and other default plugins.

```bash
llm plugins
```

--------------------------------

### Install and Use a Configurable Toolbox with LLM

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Explains how to install a toolbox plugin (e.g., `llm-tools-datasette`) and use a configured toolbox by passing a tool specification, demonstrating its use to query a Datasette instance with debug output.

```bash
llm install llm-tools-datasette
llm -T 'Datasette("https://datasette.io/content")' "Show tables" --td
```

--------------------------------

### List Installed LLM Fragment Loaders

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

This command sequence first installs the `llm-fragments-github` plugin and then lists all available fragment prefixes provided by installed plugins. It also displays documentation for each loader, detailing its purpose and expected arguments.

```bash
llm install llm-fragments-github
llm fragments loaders
```

--------------------------------

### Listing LLM Models (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/plugins/installing-plugins.md

This command displays a list of all available models, including those provided by installed plugins. It helps users identify which models are ready for use with LLM.

```bash
llm models
```

--------------------------------

### Test LLM Plugin with Prompt

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Command to execute the newly installed `markov` model with a sample prompt, demonstrating its initial 'hello world' output.

```bash
llm -m markov "the cat sat on the mat"
```

--------------------------------

### Install and Use LLM Gemini Plugin

Source: https://github.com/simonw/llm/blob/main/docs/index.md

Steps to install the LLM plugin for Google Gemini, configure the API key, and run a prompt using a Gemini model.

```bash
llm install llm-gemini
llm keys set gemini
# Paste Gemini API key here
llm -m gemini-2.0-flash 'Tell me fun facts about Mountain View'
```

--------------------------------

### Install LLM Plugin from Local File or URL

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Demonstrates how to install an LLM plugin from a locally built `.whl` file, a remote URL pointing to a `.whl` file, or a GitHub Gist ZIP archive.

```bash
llm install dist/llm_markov-0.1-py3-none-any.whl
```

```bash
llm install 'https://.../llm_markov-0.1-py3-none-any.whl'
```

```bash
llm install 'https://gist.github.com/simonw/6e56d48dc2599bffba963cef0db27b6d/archive/cc50c854414cb4deab3e3ab17e7e1e07d45cba0c.zip'
```

--------------------------------

### Create LLM Plugin Directory

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Initial setup for an LLM plugin: create the `llm-markov` directory and navigate into it.

```bash
mkdir llm-markov
cd llm-markov
```

--------------------------------

### Listing Available LLM Templates

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

Shows how to list all templates currently available to the `llm` tool. The second code block provides an example of the command's typical output format.

```Bash
llm templates
```

```Bash
cmd        : system: reply with macos terminal commands only, no extra information
glados     : system: You are GlaDOS prompt: Summarize this:
```

--------------------------------

### Listing Installed LLM Plugins (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/plugins/installing-plugins.md

This command lists all plugins currently installed and recognized by the LLM tool. It provides an overview of the active extensions and their versions.

```bash
llm plugins
```

--------------------------------

### Install llm-docs Plugin

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This command installs the `llm-docs` plugin, which provides access to the LLM documentation as a prompt fragment for answering questions.

```bash
llm install llm-docs
```

--------------------------------

### Listing LLM Models with Options (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/plugins/installing-plugins.md

This command extends the llm models output by including detailed options available for each listed model. It provides more granular information for configuring model interactions.

```bash
llm models --options
```

--------------------------------

### llm install --help

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Installs Python packages from PyPI into the same environment as LLM. It provides options for upgrading packages, installing in editable mode, forcing reinstallation, disabling cache, and including pre-release versions.

```APIDOC
Usage: llm install [OPTIONS] [PACKAGES]...

  Install packages from PyPI into the same environment as LLM

Options:
  -U, --upgrade        Upgrade packages to latest version
  -e, --editable TEXT  Install a project in editable mode from this path
  --force-reinstall    Reinstall all packages even if they are already up-to-
                       date
  --no-cache-dir       Disable the cache
  --pre                Include pre-release and development versions
  -h, --help           Show this message and exit.
```

--------------------------------

### Prepare and Upload Python Plugin to PyPI

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Installs `twine` and then uses it to upload the generated distribution packages to the Python Package Index (PyPI).

```bash
python -m pip install twine
```

```bash
python -m twine upload dist/*
```

--------------------------------

### Installing LLM Plugins using llm install (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/plugins/installing-plugins.md

This command installs a specified LLM plugin (e.g., llm-gpt4all) into the correct virtual environment. It acts as a wrapper around pip install to ensure plugins are installed where LLM can find them.

```bash
llm install llm-gpt4all
```

--------------------------------

### Install llm-templates-github Plugin

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This command installs the `llm-templates-github` plugin, enabling the use and sharing of LLM templates directly from GitHub repositories.

```bash
llm install llm-templates-github
```

--------------------------------

### Install and Use a Plugin Tool with LLM

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Demonstrates how to install a plugin that provides tools (e.g., `llm-tools-simpleeval`) and then use a specific tool from that plugin with the `--tool` option, enabling debug output for the tool's operation.

```bash
llm install llm-tools-simpleeval
llm --tool simple_eval "4444 * 233423" --td
```

--------------------------------

### Create LLM Templates with System Prompts and Piped Input

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

This example illustrates how to define an `llm` template with a `system` prompt that includes a variable, `$voice`. It also demonstrates combining standard input (piped from `curl` and `strip-tags`) with a command-line parameter to control the output's voice. This setup is useful for processing external text with specific stylistic requirements.

```YAML
system: Summarize this text in the voice of $voice
```

```Bash
curl -s 'https://til.simonwillison.net/macos/imovie-slides-and-audio' | \
  strip-tags -m | llm -t summarize -p voice GlaDOS
```

--------------------------------

### Install Pre-Release Packages with llm install --pre

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm install` command now includes a `--pre` option, enabling users to install pre-release packages, which is useful for testing new features or accessing the latest development versions.

```CLI
llm install --pre <package_name>
```

--------------------------------

### Running Prompt with Specific LLM Model (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/plugins/installing-plugins.md

This command executes a text prompt against a specified LLM model using the -m or --model option. It demonstrates how to interact with a newly installed or chosen model for generating responses.

```bash
llm -m orca-mini-3b-gguf2-q4_0 'What is the capital of France?'
```

--------------------------------

### Install LLM Plugin from Path

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Alternative command to install an LLM plugin from a specified directory path in editable mode.

```bash
llm install -e path/to/llm-markov
```

--------------------------------

### Installing Project and Test Dependencies - Bash

Source: https://github.com/simonw/llm/blob/main/docs/contributing.md

Installs the project's editable version along with its test dependencies using pip. This command ensures all required packages are available for development and running tests.

```bash
pip install -e '.[test]'
```

--------------------------------

### Install Python Build Tool

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Installs the `build` package, which is used to create distributable Python packages (wheels and sdist).

```bash
python -m pip install build
```

--------------------------------

### Install LLM CLI Tool

Source: https://github.com/simonw/llm/blob/main/README.md

Instructions for installing the LLM command-line tool using various package managers like pip, Homebrew, pipx, and uv.

```bash
pip install llm
```

```bash
brew install llm
```

```bash
pipx install llm
```

```bash
uv tool install llm
```

--------------------------------

### Set and View Default LLM Model

Source: https://github.com/simonw/llm/blob/main/docs/setup.md

This section explains how to change the default model used by the `llm` command-line tool for generating responses. Users can specify any supported model alias and also view the currently configured default model.

```bash
llm models default gpt-4o
```

```bash
llm models default
```

--------------------------------

### Start LLM chat with initial fragments

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

Demonstrates initiating an LLM chat session with pre-loaded fragments using the `-f` or `--sf` arguments. This sets up the initial chat context with the document content.

```bash
llm chat -f my_doc.txt
```

--------------------------------

### Example Usage: Printing Words from Markov Chain in Python

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

This example demonstrates how to use the `generate()` function to produce a sequence of words from a Markov chain. It shows how to first build a lookup table (assuming `build_markov_table` is defined) and then iterate over the generated words, printing each one individually.

```Python
lookup = build_markov_table("the cat sat on the mat")
for word in generate(transitions, 20):
    print(word)
```

--------------------------------

### Install LLM CLI Tool

Source: https://github.com/simonw/llm/blob/main/docs/index.md

Instructions for installing the LLM command-line interface using various popular package managers like pip, Homebrew, pipx, or uv.

```bash
pip install llm
```

```bash
brew install llm
```

```bash
pipx install llm
```

```bash
uv tool install llm
```

--------------------------------

### Install LLM Template Loader Plugin

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

This command demonstrates how to install the `llm-templates-github` plugin, which extends the `llm` tool's capabilities by adding a `gh:` prefix for loading templates directly from GitHub repositories. This simplifies the process of sharing and using community-contributed templates.

```Bash
llm install llm-templates-github
```

--------------------------------

### Install llm-templates-fabric Plugin

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This command installs the `llm-templates-fabric` plugin, which allows loading LLM templates from Daniel Miessler's Fabric collection.

```bash
llm install llm-templates-fabric
```

--------------------------------

### Integrate and Use Google Gemini with LLM CLI

Source: https://github.com/simonw/llm/blob/main/README.md

Steps to install the LLM Gemini plugin, configure your API key, and execute prompts against Google Gemini models.

```bash
llm install llm-gemini
```

```bash
llm keys set gemini
# Paste Gemini API key here
```

```bash
llm -m gemini-2.0-flash 'Tell me fun facts about Mountain View'
```

--------------------------------

### Utilize Models from LLM Plugins

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Demonstrates how to import and use models provided by installed LLM plugins, like Anthropic's Claude 3.5 Sonnet. Includes an example of setting the model's API key directly.

```python
import llm

model = llm.get_model("claude-3.5-sonnet")
# Use this if you have not set the key using 'llm keys set claude':
model.key = 'YOUR_API_KEY_HERE'
response = model.prompt("Five surprising names for a pet pelican")
print(response.text())
```

--------------------------------

### Define a Stateful Toolbox Class for Key-Value Memory

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Demonstrates how to define tools as a class by extending `llm.Toolbox`. This approach allows for bundling multiple tools, configuring them, and persisting shared state across tool invocations. The example shows a `Memory` toolbox with methods for setting, getting, appending, and listing keys in an in-memory dictionary.

```Python
import llm

class Memory(llm.Toolbox):
    _memory = None

    def _get_memory(self):
        if self._memory is None:
            self._memory = {}
        return self._memory

    def set(self, key: str, value: str):
        "Set something as a key"
        self._get_memory()[key] = value

    def get(self, key: str):
        "Get something from a key"
        return self._get_memory().get(key) or ""

    def append(self, key: str, value: str):
        "Append something as a key"
        memory = self._get_memory()
        memory[key] = (memory.get(key) or "") + "\n" + value

    def keys(self):
        "Return a list of keys"
        return list(self._get_memory().keys())
```

--------------------------------

### Manage LLM SQLite Logging Behavior

Source: https://github.com/simonw/llm/blob/main/docs/setup.md

This section details how to enable or disable the automatic logging of every prompt and response to a SQLite database by the `llm` tool. Users can also check the current status of the logging setting.

```bash
llm logs off
```

```bash
llm logs on
```

```bash
llm logs status
```

--------------------------------

### Example Interactive Chat Session Output

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

An example of an interactive chat session with a model, demonstrating the prompt and response flow within the `llm chat` interface. It shows how to type commands like `exit` or `!multi` and how the model responds.

```console
Chatting with gpt-4
Type 'exit' or 'quit' to exit
Type '!multi' to enter multiple lines, then '!end' to finish
Type '!edit' to open your default editor and modify the prompt
Type '!fragment <my_fragment> [<another_fragment> ...]' to insert one or more fragments
> who are you?
I am a sentient cheesecake, meaning I am an artificial
intelligence embodied in a dessert form, specifically a
cheesecake. However, I don't consume or prepare foods
like humans do, I communicate, learn and help answer
your queries.
```

--------------------------------

### Example Output of llm plugins

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

JSON output showing the expected result of `llm plugins`, including the `llm-markov` plugin details and default LLM plugins.

```json
[
  {
    "name": "llm-markov",
    "hooks": [
      "register_models"
    ],
    "version": "0.1"
  },
  {
    "name": "llm.default_plugins.openai_models",
    "hooks": [
      "register_commands",
      "register_models"
    ]
  }
]
```

--------------------------------

### Install and Use LLM Anthropic Plugin

Source: https://github.com/simonw/llm/blob/main/docs/index.md

Steps to install the LLM plugin for Anthropic's Claude, configure the API key, and run a prompt using a Claude model.

```bash
llm install llm-anthropic
llm keys set anthropic
# Paste Anthropic API key here
llm -m claude-4-opus 'Impress me with wild facts about turnips'
```

--------------------------------

### Setting Up Virtual Environment with pipenv - Bash

Source: https://github.com/simonw/llm/blob/main/docs/contributing.md

Activates the pipenv shell for the project, which automatically manages dependencies and the virtual environment. This provides an alternative to manual venv setup.

```bash
pipenv shell
```

--------------------------------

### Install Ollama Plugin for Local LLM Models

Source: https://github.com/simonw/llm/blob/main/README.md

How to install the LLM Ollama plugin to enable interaction with local language models running via Ollama.

```bash
# Install the plugin
llm install llm-ollama
```

--------------------------------

### Install LLM Plugin in Editable Mode

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Command to install the plugin from the current directory in editable mode, allowing live code changes without reinstallation.

```bash
llm install -e .
```

--------------------------------

### Configure Custom LLM Data Directory Location

Source: https://github.com/simonw/llm/blob/main/docs/setup.md

This section describes how to set a custom location for the `llm` tool's data directory, which stores various files like prompt templates, stored keys, preferences, and a database of logs. This is achieved by setting the `LLM_USER_PATH` environment variable.

```bash
export LLM_USER_PATH=/path/to/my/custom/directory
```

--------------------------------

### List All Available LLM Model Options

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Display all configurable options for the currently installed `llm` models. Options may vary depending on the specific model.

```Shell
llm models list --options
```

--------------------------------

### Query LLM Documentation with llm-docs Plugin

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This command demonstrates how to use the `llm-docs` plugin to query the LLM documentation. The `docs:` prefix registers the plugin to fetch documentation for the installed LLM version and use it as a prompt fragment.

```bash
llm -f docs: 'How do I save a new template?'
```

--------------------------------

### Configure pyproject.toml for LLM Plugin Metadata

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Example `pyproject.toml` configuration for an LLM plugin, including project metadata, dependencies, license, and entry points for PyPI distribution. This ensures proper display on PyPI and manages dependencies.

```toml
[project]
name = "llm-markov"
version = "0.1"
description = "Plugin for LLM adding a Markov chain generating model"
readme = "README.md"
authors = [{name = "Simon Willison"}]
license = {text = "Apache-2.0"}
classifiers = [
    "License :: OSI Approved :: Apache Software License"
]
dependencies = [
    "llm"
]
requires-python = ">3.7"

[project.urls]
Homepage = "https://github.com/simonw/llm-markov"
Changelog = "https://github.com/simonw/llm-markov/releases"
Issues = "https://github.com/simonw/llm-markov/issues"

[project.entry-points.llm]
markov = "llm_markov"
```

--------------------------------

### Extract First Fenced Code Block from LLM Logs

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

This command extracts and returns the content of the first fenced code block found within the selected log entries. It's useful for quickly getting code examples from responses.

```bash
llm logs --extract
```

--------------------------------

### Start Chat with Saved Template

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Shows how to initiate a new chat session using a previously saved template with the `-t` flag. This is convenient for quickly launching conversations with predefined personas or settings.

```bash
llm chat -t cheesecake
```

--------------------------------

### Embed and Search Binary Data with LLM CLIP

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

LLM's embedding feature now supports binary data, enabling multimodal models like CLIP to embed images and text into a shared vector space. This allows for semantic search of images based on text queries. The example demonstrates installing the `llm-clip` plugin, embedding JPEGs, and then searching for specific content.

```bash
llm install llm-clip
llm embed-multi photos --files photos/ '*.jpg' --binary -m clip
```

```bash
llm similar photos -c 'raccoon'
```

```json
{"id": "IMG_4801.jpeg", "score": 0.28125139257127457, "content": null, "metadata": null}
{"id": "IMG_4656.jpeg", "score": 0.26626441704164294, "content": null, "metadata": null}
{"id": "IMG_2944.jpeg", "score": 0.2647445926996852, "content": null, "metadata": null}
...
```

--------------------------------

### Install and Use llm-sentence-transformers Plugin for Local Embeddings

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Shows how to install the `llm-sentence-transformers` plugin and then use it to calculate embeddings with a local model like MiniLM-L6. This allows running models on your own laptop.

```bash
llm install llm-sentence-transformers
```

```bash
llm embed -c 'This is some content' -m sentence-transformers/all-MiniLM-L6-v2
```

--------------------------------

### Use System Prompt Fragment from File using llm

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Demonstrates how to use the '--sf' or '--system-fragment' option to load a system prompt from a file (explain_code.txt). This allows for predefined system instructions to guide the model's behavior, such as instructing it to explain code in detail, ensuring consistent model responses.

```bash
llm -f cli.py --sf explain_code.txt
```

--------------------------------

### List Available Plugin Tools in LLM

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Shows the command to list all tools that have been made available through installed plugins, helping users discover available functionalities.

```bash
llm tools
```

--------------------------------

### Install llm-gpt4all Plugin for Local Models

Source: https://github.com/simonw/llm/blob/main/docs/other-models.md

This command installs the `llm-gpt4all` plugin, which provides access to 17 models from the GPT4All project. This enables LLM to use local models directly on your machine.

```bash
llm install llm-gpt4all
```

--------------------------------

### Install strip-tags Tool for HTML Processing

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

Provides the command to install the `strip-tags` utility, a tool used to remove HTML tags from content. This is useful for reducing input size for LLMs, especially when dealing with large web pages, to avoid exceeding token limits. The command uses `uv tool install`.

```bash
uv tool install strip-tags
```

--------------------------------

### llm plugins --help

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Lists all installed LLM plugins. Users can choose to include built-in default plugins in the list or filter plugins by a specific hook they implement.

```APIDOC
Usage: llm plugins [OPTIONS]

  List installed plugins

Options:
  --all        Include built-in default plugins
  --hook TEXT  Filter for plugins that implement this hook
  -h, --help   Show this message and exit.
```

--------------------------------

### Install LLM Plugin from Local Directory

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Install an `llm` plugin directly from a local file system directory. This is useful for developing or testing plugins locally before publishing.

```Shell
llm install -e directory
```

--------------------------------

### Integrate and Use Anthropic Claude with LLM CLI

Source: https://github.com/simonw/llm/blob/main/README.md

Instructions for installing the LLM Anthropic plugin, setting up your API key, and running prompts with Anthropic Claude models.

```bash
llm install llm-anthropic
```

```bash
llm keys set anthropic
# Paste Anthropic API key here
```

```bash
llm -m claude-4-opus 'Impress me with wild facts about turnips'
```

--------------------------------

### List all available LLM models using `llm models`

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

This command lists every model that can be used with LLM, including those installed via plugins, along with their aliases.

```bash
llm models
```

--------------------------------

### Example LLM Output with Defined JSON Schema

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

An example of the JSON output generated by the `llm` tool when provided with the specific JSON schema for a 'dog' object.

```json
{
  "name": "Baxter",
  "age": 3,
  "one_sentence_bio": "Baxter is a rescue dog who learned to skateboard and now performs tricks at local parks, astonishing everyone with his skill!"
}
```

--------------------------------

### Install and Use LLM Ollama Plugin for Local Models

Source: https://github.com/simonw/llm/blob/main/docs/index.md

Instructions to install the LLM plugin for Ollama, pull a local model (e.g., Llama 3.2), and run a prompt against it on your local machine.

```bash
# Install the plugin
llm install llm-ollama

# Download and run a prompt against the Orca Mini 7B model
ollama pull llama3.2:latest
llm -m llama3.2:latest 'What is the capital of France?'
```

--------------------------------

### Install LLM Model Plugins

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Instructions for installing LLM plugins, such as `llm-anthropic`, using pip. Plugins extend the LLM library with support for additional language models.

```bash
pip install llm-anthropic
```

--------------------------------

### Example of an Interactive llm Chat Session

Source: https://github.com/simonw/llm/blob/main/README.md

This example illustrates the user experience within an active `llm chat` session. It details the commands available for session control (e.g., `exit`, `!multi`, `!edit`, `!fragment`) and provides a sample interaction where a user asks a joke and the model responds.

```default
Chatting with gpt-4.1
Type 'exit' or 'quit' to exit
Type '!multi' to enter multiple lines, then '!end' to finish
Type '!edit' to open your default editor and modify the prompt.
Type '!fragment <my_fragment> [<another_fragment> ...]' to insert one or more fragments
> Tell me a joke about a pelican
Why don't pelicans like to tip waiters?

Because they always have a big bill!
```

--------------------------------

### Build Local HTML Documentation for Python Project

Source: https://github.com/simonw/llm/blob/main/AGENTS.md

These commands navigate into the 'docs' directory, install the required Python packages for documentation generation (e.g., Sphinx, themes), and then compile the documentation into HTML format. The generated HTML files can then be viewed locally in a web browser.

```bash
cd docs
pip install -r requirements.txt
make html
```

--------------------------------

### Example JSON Data for LLM Output

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

An example of structured JSON data, typically generated as output from an LLM, showing details about individuals.

```json
{"name": "Gayle King", "organization": "Blue Origin", "role": "TV Journalist", "learned": "She is participating in the upcoming Blue Origin spaceflight."}
```

--------------------------------

### Uninstall LLM Plugin

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Uninstalls a previously installed LLM plugin, useful for testing different installation methods.

```bash
llm uninstall llm-markov -y
```

--------------------------------

### Install and Use GitHub Fragment Plugin

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

This snippet demonstrates how to install the `llm-fragments-github` plugin and then use it to load fragments directly from a public GitHub repository. The plugin converts repository files into fragments, allowing `llm` to answer questions about the repository's content.

```bash
llm install llm-fragments-github
llm -f github:simonw/s3-credentials 'Suggest new features for this tool'
```

--------------------------------

### Example LLM Log Entry with Options

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Provides a JSON representation of a single LLM log entry, demonstrating how custom options like `length` and `delay` are recorded in the `options_json` field for auditing and debugging.

```json
[
  {
    "id": 636,
    "model": "markov",
    "prompt": "the cat sat on the mat",
    "system": null,
    "prompt_json": null,
    "options_json": {
      "length": 20,
      "delay": 0.1
    },
    "response": "the mat on the mat on the cat sat on the mat sat on the mat cat sat on the ",
    "response_json": null,
    "reply_to_id": null,
    "chat_id": null,
    "duration_ms": 2063,
    "datetime_utc": "2023-07-07T03:02:28.232970"
  }
]
```

--------------------------------

### Pulling a Model and Running a Prompt with llm

Source: https://github.com/simonw/llm/blob/main/README.md

This snippet demonstrates the initial steps to use the `llm` CLI tool: first, pulling a specific language model (e.g., `llama3.2:latest`) using `ollama`, and then executing a text prompt against the downloaded model to get a response directly from the command line.

```bash
ollama pull llama3.2:latest
llm -m llama3.2:latest 'What is the capital of France?'
```

--------------------------------

### Interactive Session with LLM Memory Tool

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-hooks.md

This detailed example provides an interactive chat session demonstrating the functionality of the `Memory` tool. It showcases how to set, retrieve, list, and append values using the tool's methods within a conversational context.

```bash
Chatting with gpt-4.1-mini
Type 'exit' or 'quit' to exit
Type '!multi' to enter multiple lines, then '!end' to finish
Type '!edit' to open your default editor and modify the prompt
Type '!fragment <my_fragment> [<another_fragment> ...]' to insert one or more fragments
> Remember my name is Henry

Tool call: Memory_set({'key': 'user_name', 'value': 'Henry'})
  null

Got it, Henry! I'll remember your name. How can I assist you today?
> what keys are there?

Tool call: Memory_keys({})
  [
    "user_name"
  ]

Currently, there is one key stored: "user_name". Would you like to add or retrieve any information?
> read it

Tool call: Memory_get({'key': 'user_name'})
  Henry

The value stored under the key "user_name" is Henry. Is there anything else you'd like to do?
> add Barrett to it

Tool call: Memory_append({'key': 'user_name', 'value': 'Barrett'})
  null

I have added "Barrett" to the key "user_name". If you want, I can now show you the updated value.
> show value

Tool call: Memory_get({'key': 'user_name'})
  Henry
  Barrett

The value stored under the key "user_name" is now:
Henry
Barrett

Is there anything else you would like to do?
```

--------------------------------

### Install Python Project with Test Dependencies

Source: https://github.com/simonw/llm/blob/main/AGENTS.md

This command installs the Python project in editable mode, ensuring that local changes are reflected without reinstallation. It also includes the 'test' extra, pulling in all necessary dependencies for running the project's test suite.

```bash
pip install -e '.[test]'
```

--------------------------------

### LLM YAML Template with Combined System and Regular Prompt

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

An example demonstrating the combination of both `system` and `prompt` keys in a YAML template, allowing for both model behavior instructions and specific user input processing within the same template.

```yaml
system: You speak like an excitable Victorian adventurer
prompt: 'Summarize this: $input'
```

--------------------------------

### Prompting GPT-4o Mini Model via llm CLI

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Demonstrates how to use the `llm` command-line tool to interact with the new `gpt-4o-mini` model. This example shows a simple text prompt in French.

```bash
llm -m gpt-4o-mini 'rave about pelicans in French'
```

--------------------------------

### llm CLI Global Help and Commands Overview

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Provides a comprehensive overview of the `llm` command-line tool, including its general usage, global options, and a list of all available subcommands with brief descriptions. It serves as the entry point for understanding the `llm` CLI.

```APIDOC
Usage: llm [OPTIONS] COMMAND [ARGS]...

  Access Large Language Models from the command-line

  Documentation: https://llm.datasette.io/

  LLM can run models from many different providers. Consult the plugin directory
  for a list of available models:

  https://llm.datasette.io/en/stable/plugins/directory.html

  To get started with OpenAI, obtain an API key from them and:

      $ llm keys set openai
      Enter key: ...

  Then execute a prompt like this:

      llm 'Five outrageous names for a pet pelican'

  For a full list of prompting options run:

      llm prompt --help

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  prompt*       Execute a prompt
  aliases       Manage model aliases
  chat          Hold an ongoing chat with a model.
  collections   View and manage collections of embeddings
  embed         Embed text and store or return the result
  embed-models  Manage available embedding models
  embed-multi   Store embeddings for multiple strings at once in the...
  fragments     Manage fragments that are stored in the database
  install       Install packages from PyPI into the same environment as LLM
  keys          Manage stored API keys for different models
  logs          Tools for exploring logged prompts and responses
  models        Manage available models
  openai        Commands for working directly with the OpenAI API
  plugins       List installed plugins
  schemas       Manage stored schemas
  similar       Return top N similar IDs from a collection using cosine...
  templates     Manage stored prompt templates
  tools         Manage tools that can be made available to LLMs
  uninstall     Uninstall Python packages from the LLM environment
```

--------------------------------

### Running Model with Length and Delay Options

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Demonstrates how to execute the Markov model from the command line, specifying both the desired `length` of the generated text and a `delay` between tokens to simulate streaming output.

```bash
llm -m markov "the cat sat on the mat" \
  -o length 20 -o delay 0.1
```

--------------------------------

### Example Output: People Extraction from Web Article

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

This JSON object shows an example of the structured data extracted by the `llm` tool using the 'people' template from a web article. It contains an array of 'items', each representing a person with detailed attributes.

```json
{
  "items": [
    {
      "name": "Billy McFarland",
      "organization": "Fyre Festival",
      "role": "Organiser",
      "learned": "Billy McFarland is known for organizing the infamous Fyre Festival and was sentenced to six years in prison for wire fraud related to it. He is attempting to revive the festival with Fyre 2.",
      "article_headline": "Welcome back Billy McFarland and a new Fyre festival. Shows you can’t keep a good fantasist down",
      "article_date": "2025-02-27"
    }
  ]
}
```

--------------------------------

### Example Output: People Extraction from Image

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

This JSON object presents an example of structured data extracted by the `llm` tool from an image attachment. It contains an array of 'items', each detailing a person and their associated information from the image content.

```json
{
  "items": [
    {
      "name": "Mark Zuckerberg",
      "organization": "Facebook",
      "role": "CEO",
      "learned": "He addressed criticism by suggesting anyone with similar values and thirst for power could make the same mistakes.",
      "article_headline": "Mark Zuckerberg Insists Anyone With Same Skewed Values And Unrelenting Thirst For Power Could Have Made Same Mistakes",
      "article_date": "2018-06-14"
    }
  ]
}
```

--------------------------------

### Example Output from LLM Markov Plugin Execution

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

This snippet shows a sample of the text output generated by the Markov chain LLM plugin when executed with a specific prompt. It illustrates the randomized, chain-based text that the model produces based on the input training data.

```Text
the mat the cat sat on the cat sat on the mat cat sat on the mat cat sat on
```

--------------------------------

### Explore SQLite Database with Datasette Web UI

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

Commands to launch Datasette, a web interface for exploring SQLite databases, allowing interactive navigation of the `data.db` file.

```bash
uvx datasette data.db
# Or install datasette first:
uv tool install datasette # or pip install or pipx install
datasette data.db
```

--------------------------------

### Example Output: LLM Models with Custom Model

Source: https://github.com/simonw/llm/blob/main/docs/openai-models.md

This example output from `llm models` shows how a custom-added OpenAI model, `gpt-3.5-turbo-0613` with alias `0613`, appears in the list of available models. This confirms successful integration of the custom model into the LLM environment.

```bash
OpenAI Chat: gpt-3.5-turbo (aliases: 3.5, chatgpt)
OpenAI Chat: gpt-3.5-turbo-16k (aliases: chatgpt-16k, 3.5-16k)
OpenAI Chat: gpt-4 (aliases: 4, gpt4)
OpenAI Chat: gpt-4-32k (aliases: 4-32k)
OpenAI Chat: gpt-3.5-turbo-0613 (aliases: 0613)
```

--------------------------------

### Use Specific LLM Models (CLI)

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Example of using the `-m` option to specify a particular model, such as GPT-4.5 preview, for a prompt.

```Bash
llm -m gpt-4.5 'a joke about a pelican and a wolf'
```

--------------------------------

### Registering and Implementing a Single Fragment Loader

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-hooks.md

This Python example demonstrates how to register a custom fragment loader using the `llm.hookimpl` decorator. The `my_fragment_loader` function shows how to return a single `llm.Fragment` object, including content and an optional source, and how to handle potential loading errors by raising a `ValueError`.

```python
import llm

@llm.hookimpl
def register_fragment_loaders(register):
    register("my-fragments", my_fragment_loader)


def my_fragment_loader(argument: str) -> llm.Fragment:
    """
    Documentation for the fragment loader goes here. It will be displayed
    when users run the 'llm fragments loaders' command.
    """
    try:
        fragment = "Fragment content for {}".format(argument)
        source = "my-fragments:{}".format(argument)
        return llm.Fragment(fragment, source)
    except Exception as ex:
        # Raise a ValueError with a clear message if the fragment cannot be loaded
        raise ValueError(
            f"Fragment 'my-fragments:{argument}' could not be loaded: {str(ex)}"
        )
```

--------------------------------

### Example output of browsing LLM fragments

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

Provides a sample YAML output from the `llm fragments` command, detailing the structure of stored fragment information including hash IDs, aliases, datetime, source, and truncated content.

```yaml
- hash: 0d6e368f9bc21f8db78c01e192ecf925841a957d8b991f5bf9f6239aa4d81815
  aliases: []
  datetime_utc: '2025-04-06 07:36:53'
  source: https://raw.githubusercontent.com/simonw/llm-docs/refs/heads/main/llm/0.22.txt
  content: |-
    <documents>
    <document index="1">
    <source>docs/aliases.md</source>
    <document_content>
    (aliases)=
    #...
- hash: 16b686067375182573e2aa16b5bfc1e64d48350232535d06444537e51f1fd60c
  aliases: []
  datetime_utc: '2025-04-06 23:03:47'
  source: simonw/files-to-prompt/pyproject.toml
  content: |-
    [project]
    name = "files-to-prompt"
    version = "0.6"
    description = "Concatenate a directory full of..."
```

--------------------------------

### Start Interactive LLM Chat Session

Source: https://github.com/simonw/llm/blob/main/docs/index.md

Initiates an interactive chat session with a specified language model, allowing for multi-turn conversations directly from the command line.

```bash
llm chat -m gpt-4.1
```

--------------------------------

### OpenAI Completion Model: gpt-3.5-turbo-instruct API Reference

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the OpenAI gpt-3.5-turbo-instruct completion model, including detailed descriptions for each configurable option and supported features like streaming.

```APIDOC
OpenAI Completion: gpt-3.5-turbo-instruct (aliases: 3.5-instruct, chatgpt-instruct)
  Options:
    temperature: float
      What sampling temperature to use, between 0 and 2. Higher values like
      0.8 will make the output more random, while lower values like 0.2 will
      make it more focused and deterministic.
    max_tokens: int
      Maximum number of tokens to generate.
    top_p: float
      An alternative to sampling with temperature, called nucleus sampling,
      where the model considers the results of the tokens with top_p
      probability mass. So 0.1 means only the tokens comprising the top 10%
      probability mass are considered. Recommended to use top_p or
      temperature but not both.
    frequency_penalty: float
      Number between -2.0 and 2.0. Positive values penalize new tokens based
      on their existing frequency in the text so far, decreasing the model's
      likelihood to repeat the same line verbatim.
    presence_penalty: float
      Number between -2.0 and 2.0. Positive values penalize new tokens based
      on whether they appear in the text so far, increasing the model's
      likelihood to talk about new topics.
    stop: str
      A string where the API will stop generating further tokens.
    logit_bias: dict, str
      Modify the likelihood of specified tokens appearing in the completion.
      Pass a JSON string like '{"1712":-100, "892":-100, "1489":-100}'
    seed: int
      Integer seed to attempt to sample deterministically
    logprobs: int
      Include the log probabilities of most likely N per token
  Features:
  - streaming
```

--------------------------------

### Provide Context with Prompt Fragments

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Understand how to pass `fragments` and `system_fragments` lists to the `model.prompt()` method. This allows injecting external document content or system-level instructions to guide the LLM's response.

```python
response = model.prompt(
    "What do these documents say about dogs?",
    fragments=[
        open("dogs1.txt").read(),
        open("dogs2.txt").read()
    ],
    system_fragments=[
        "You answer questions like Snoopy"
    ]
)
```

--------------------------------

### Example Output from SQLite Query

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

The tabular output showing name, organization, and role for various individuals, generated by the `sqlite-utils rows` command.

```text
name             organization        role
---------------  ------------------  -----------------------------------------
Katy Perry       Blue Origin         Singer
Gayle King       Blue Origin         TV Journalist
Lauren Sanchez   Blue Origin         Helicopter Pilot and former TV Journalist
Aisha Bowe       Engineering firm    Former NASA Rocket Scientist
Amanda Nguyen    Research Scientist  Activist and Scientist
Kerianne Flynn   Movie Producer      Producer
Billy McFarland  Fyre Festival       Organiser
Mark Zuckerberg  Facebook            CEO
```

--------------------------------

### Testing Option Validation (Invalid Length)

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Provides a command-line example to test the validation rules for the `length` option, demonstrating how an invalid input (e.g., -1) triggers a Pydantic `ValueError`.

```bash
llm -m markov "the cat sat on the mat" -o length -1
```

--------------------------------

### Prompting OpenAI Models with llm Python API

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Illustrates how to use the `llm` Python API to get an OpenAI model instance (`gpt-4o-mini`) and send a simple text prompt. This method now correctly picks up API keys configured via `llm keys set` or `OPENAI_API_KEY`.

```python
import llm
print(llm.get_model("gpt-4o-mini").prompt("hi"))
```

--------------------------------

### Verifying Plugin Loading with Environment Variable (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/plugins/installing-plugins.md

This command verifies the effect of the LLM_LOAD_PLUGINS environment variable by running llm plugins after setting it to an empty string. The output should reflect that no plugins are loaded, confirming the environment variable's effect.

```bash
LLM_LOAD_PLUGINS='' llm plugins
```

--------------------------------

### Combine piped content with a system prompt in llm

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Pipes content (e.g., from a URL) and combines it with a system prompt. The system prompt guides the model on how to process the piped input, such as formatting output as JSON.

```bash
curl -s 'https://simonwillison.net/2023/May/15/per-interpreter-gils/' | \
  llm -s 'Suggest topics for this post as a JSON array'
```

--------------------------------

### Specify Output Schemas for LLM Prompts (CLI)

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Demonstrates various command-line options for providing JSON schemas or concise schema specifications to guide the LLM model's output.

```Bash
llm prompt --schema '{JSON schema goes here}'
```

```Bash
llm prompt --schema 'name, bio, age int'
```

--------------------------------

### Start a New LLM Chat Conversation

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This command initiates a new chat conversation with the LLM, providing an initial prompt. The model will generate a response based on this input, establishing the context for subsequent interactions.

```bash
llm "Pretend to be a witty gerbil, say hi briefly"
```

--------------------------------

### llm keys Command Line Interface Reference

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Reference for the `llm keys` command, used to manage API keys for different models, including listing, getting, setting, and showing the key file path.

```APIDOC
Usage: llm keys [OPTIONS] COMMAND [ARGS]...

  Manage stored API keys for different models

Options:
  -h, --help  Show this message and exit.

Commands:
  list*  List names of all stored keys
  get    Return the value of a stored key
  path   Output the path to the keys.json file
  set    Save a key in the keys.json file
```

--------------------------------

### Example Usage: Generating a Full Sentence from Markov Chain in Python

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

This snippet illustrates how to combine the words generated by the Markov chain into a single string sentence. It uses Python's `join()` method to concatenate the yielded words with spaces, creating a complete and readable output string.

```Python
sentence = " ".join(generate(transitions, 20))
```

--------------------------------

### Multi-line LLM YAML Prompt Template with `>`

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

An example of a multi-line YAML template using `prompt: >` to define a longer, formatted prompt. This syntax treats indented text as a single string, collapsing newlines into spaces.

```yaml
prompt: >
    Summarize the following text.

    Insert frequent satirical steampunk-themed illustrative anecdotes.
    Really go wild with that.

    Text to summarize: $input
```

--------------------------------

### CLI: Prompt Output Extraction and Template Saving

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm prompt` command now supports `--extract-last` (`-xl`) to get the last fenced code block and `--extract` (`-x`) to get the first. These options can also be saved within YAML templates.

```Shell
llm prompt --xl 'Python function to reverse a string'
llm prompt -x 'Python function to reverse a string'
llm prompt 'Generate a YAML config' --save my_template -x
```

```YAML
extract: true
```

--------------------------------

### Executing LLM Markov Plugin from Command Line

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

This snippet provides the command-line instruction to run the newly implemented Markov chain LLM plugin. It demonstrates how to invoke the `llm` tool using the `-m markov` flag to specify the model and provide an input prompt string.

```Bash
llm -m markov "the cat sat on the mat"
```

--------------------------------

### Register Synchronous LLM Language Model

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-hooks.md

This hook enables plugins to register one or more additional synchronous language models. The example illustrates how to define and register a basic `HelloWorld` model that returns a fixed string.

```Python
import llm

@llm.hookimpl
def register_models(register):
    register(HelloWorld())

class HelloWorld(llm.Model):
    model_id = "helloworld"

    def execute(self, prompt, stream, response):
        return ["hello world"]
```

--------------------------------

### Interactive Terminal Chat with LLM

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Introduces the `llm chat` command for starting an interactive terminal chat session with a language model.

```CLI
llm chat
```

--------------------------------

### Execute Multiple Default LLM Tools via CLI

Source: https://github.com/simonw/llm/blob/main/docs/tools.md

This example illustrates how to invoke multiple default tools, `llm_version` and `llm_time`, simultaneously using the `llm` command-line interface. It demonstrates the shorthand `-T` option for specifying tools and how the model processes multiple tool calls to generate a combined response.

```bash
llm -T llm_version -T llm_time 'Give me the current time and LLM version' --td
```

--------------------------------

### Starting an LLM Conversation with Pre-defined Tools

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Illustrates how to initialize a conversation with a set of predefined tool functions. These tools become available for use throughout the conversation, allowing the model to perform specific actions based on user prompts within the conversational flow.

```python
import llm

def upper(text: str) -> str:
    "convert text to upper case"
    return text.upper()

def reverse(text: str) -> str:
    "reverse text"
    return text[::-1]

model = llm.get_model("gpt-4.1-mini")
conversation = model.conversation(tools=[upper, reverse])
```

--------------------------------

### Configure OpenAI and Run Basic Prompts

Source: https://github.com/simonw/llm/blob/main/docs/index.md

Demonstrates how to set up your OpenAI API key and execute various types of prompts, including text generation, image text extraction, and using system prompts with file input.

```bash
# Paste your OpenAI API key into this
llm keys set openai

# Run a prompt (with the default gpt-4o-mini model)
llm "Ten fun names for a pet pelican"

# Extract text from an image
llm "extract text" -a scanned-document.jpg

# Use a system prompt against a file
cat myfile.py | llm -s "Explain this code"
```

--------------------------------

### llm fragments show --help

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Displays the content of a fragment stored in the database. The fragment can be identified by its alias or its hash. An example shows how to display the 'mydocs' fragment.

```APIDOC
Usage: llm fragments show [OPTIONS] ALIAS_OR_HASH

  Display the fragment stored under an alias or hash

      llm fragments show mydocs

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Initiating an Interactive Chat Session with llm

Source: https://github.com/simonw/llm/blob/main/README.md

This command shows how to start an interactive conversational session with a specified language model, such as `gpt-4.1`, using the `llm chat` command. Once initiated, users can type multiple prompts and receive continuous responses, simulating a chat interface.

```bash
llm chat -m gpt-4.1
```

--------------------------------

### Build Python Plugin Distribution Packages

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Runs the `build` command in the plugin directory to create `tar.gz` and `.whl` distribution files.

```bash
python -m build
```

--------------------------------

### Example JSON Output from llm embed Command

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Illustrates the typical JSON array format of floating-point numbers returned by the `llm embed` command when outputting embeddings directly to the terminal.

```json
[0.123, 0.456, 0.789...]
```

--------------------------------

### Loading Specific LLM Plugins via Environment Variable (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/plugins/installing-plugins.md

This command shows how to selectively load specific LLM plugins by setting the LLM_LOAD_PLUGINS environment variable to a comma-separated list of plugin names. Only the specified plugins will be active for the subsequent LLM command.

```bash
LLM_LOAD_PLUGINS='llm-gpt4all,llm-cluster' llm ...
```

--------------------------------

### Example of a Markdown Fenced Code Block

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Illustrates the syntax of a Markdown fenced code block, which the `--extract` option in LLM can parse to retrieve only the code content, excluding the delimiters.

```markdown
```python
def my_function():
    # ...
```
```

--------------------------------

### Validation Error Output Example

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Displays the expected error message returned by the LLM command-line interface when an option fails Pydantic validation, specifically for the `length` parameter.

```text
Error: length
  Value error, length must be >= 2
```

--------------------------------

### Registering Python Classes as LLM Toolbox Tools

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-hooks.md

This example illustrates how to register a Python class, specifically one inheriting from `llm.Toolbox`, as a tool. It highlights that the class itself, not an instance, is passed to the `register()` function for the `register_tools` hook.

```python
import llm

class Memory(llm.Toolbox):
    ...

@llm.hookimpl
def register_tools(register):
    register(Memory)
```

--------------------------------

### Define a Basic LLM System Prompt Template

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This YAML snippet defines a simple prompt template that sets a system prompt. The system prompt guides the LLM's behavior, in this case, instructing it to summarize text.

```yaml
system: Summarize this text
```

--------------------------------

### Use System Prompts with LLM Python API

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Shows how to pass a system prompt to the LLM model to guide its behavior, using the `system` keyword argument. This allows for setting the persona or instructions for the model's response.

```python
response = model.prompt(
    "Five surprising names for a pet pelican",
    system="Answer like GlaDOS"
)
```

--------------------------------

### Initializing a New Conversation with LLM Models

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Explains how to start a new conversational session using the `model.conversation()` method. This method creates a conversation object that maintains context across multiple prompts, enabling follow-up questions and persistent interactions.

```python
model = llm.get_model()
conversation = model.conversation()
```

--------------------------------

### Run LLM Template with `curl` and `strip-tags`

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

Demonstrates a command-line pipeline to fetch web content using `curl`, process it with `strip-tags` to remove HTML and minify whitespace, and then pipe the cleaned text to `llm` using a specific template and model.

```bash
curl -s 'https://til.simonwillison.net/macos/imovie-slides-and-audio' | \
  strip-tags -m | llm -t steampunk -m gpt-4o
```

--------------------------------

### Register Synchronous and Asynchronous LLM Language Models with Alias

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-hooks.md

This example demonstrates how to register both synchronous and asynchronous versions of a language model, along with an alias, using the `register_models` hook. It shows the structure for an `AsyncModel` and how to pass multiple models and aliases to the register function.

```Python
class AsyncHelloWorld(llm.AsyncModel):
    model_id = "helloworld"

    async def execute(self, prompt, stream, response):
        return ["hello world"]

@llm.hookimpl
def register_models(register):
    register(HelloWorld(), AsyncHelloWorld(), aliases=("hw",))
```

--------------------------------

### Example Output: Newline-Delimited Logged Items

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

This output shows multiple JSON objects, each representing an extracted 'person' item, separated by newlines. This format is useful for processing individual records sequentially.

```json
{"name": "Katy Perry", "organization": "Blue Origin", "role": "Singer", "learned": "She is one of the passengers on the upcoming spaceflight with Blue Origin."}
{"name": "Gayle King", "organization": "Blue Origin", "role": "TV Journalist", "learned": "She is participating in the upcoming Blue Origin spaceflight."}
{"name": "Lauren Sanchez", "organization": "Blue Origin", "role": "Helicopter Pilot and former TV Journalist", "learned": "She selected the crew for the Blue Origin spaceflight."}
{"name": "Aisha Bowe", "organization": "Engineering firm", "role": "Former NASA Rocket Scientist", "learned": "She is part of the crew for the spaceflight."}
{"name": "Amanda Nguyen", "organization": "Research Scientist", "role": "Activist and Scientist", "learned": "She is included in the crew for the upcoming Blue Origin flight."}
{"name": "Kerianne Flynn", "organization": "Movie Producer", "role": "Producer", "learned": "She will also be a passenger on the upcoming spaceflight."}
{"name": "Billy McFarland", "organization": "Fyre Festival", "role": "Organiser", "learned": "He was sentenced to six years in prison for wire fraud in 2018 and has launched a new festival called Fyre 2.", "article_headline": "Welcome back Billy McFarland and a new Fyre festival. Shows you can’t keep a good fantasist down", "article_date": "2025-02-27"}
{"name": "Mark Zuckerberg", "organization": "Facebook", "role": "CEO", "learned": "He attempted to dismiss criticism by suggesting that anyone with similar values and thirst for power could have made the same mistakes.", "article_headline": "Mark Zuckerberg Insists Anyone With Same Skewed Values And Unrelenting Thirst For Power Could Have Made Same Mistakes", "article_date": "2018-06-14"}
```

--------------------------------

### Get llm Collections Database Path

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Outputs the file path to the embeddings database used by `llm` collections. This command is useful for locating where collection data is stored on the filesystem.

```Bash
Usage: llm collections path [OPTIONS]

  Output the path to the embeddings database

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Get LLM Log Database Path

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

This command reveals the file path to the SQLite database where `llm` stores all prompt and response logs. The location may vary depending on the operating system.

```bash
llm logs path
```

--------------------------------

### Example Output: Logged Items as JSON Array

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

This JSON snippet illustrates the beginning of a valid JSON array containing multiple extracted 'person' objects. This format is suitable for direct parsing as a single JSON document.

```json
[{"name": "Katy Perry", "organization": "Blue Origin", "role": "Singer", "learned": "She is one of the passengers on the upcoming spaceflight with Blue Origin."},{"name": "Gayle King", "organization": "Blue Origin", "role": "TV Journalist", "learned": "She is participating in the upcoming Blue Origin spaceflight."},{"name": "Lauren Sanchez", "organization": "Blue Origin", "role": "Helicopter Pilot and former TV Journalist", "learned": "She selected the crew for the Blue Origin spaceflight."},{"name": "Aisha Bowe", "organization": "Engineering firm", "role": "Former NASA Rocket Scientist", "learned": "She is part of the crew for the spaceflight."},{"name": "Amanda Nguyen", "organization": "Research Scientist", "role": "Activist and Scientist", "learned": "She is included in the crew for the upcoming Blue Origin flight."},{"name": "Kerianne Flynn", "organization": "Movie Producer", "role": "Producer", "learned": "She will also be a passenger on the upcoming spaceflight."},{"name": "Billy McFarland", "organization": "Fyre Festival", "role": "Organiser", "learned": "He was sentenced to six years in prison for wire fraud in 2018 and has launched a new festival called Fyre 2.", "article_headline": "Welcome back Billy McFarland and a new Fyre festival. Shows you can’t keep a good fantasist down", "article_date": "2025-02-27"},{"name": "Mark Zuckerberg", "organization": "Facebook", "role": "CEO", "learned": "He attempted to dismiss criticism by suggesting that anyone with similar values and thirst for power could have made the same mistakes.", "article_headline": "Mark Zuckerberg Insists Anyone With Same Skewed Values And Unrelenting Thirst For Power Could Have Made Same Mistakes", "article_date": "2018-06-14"}]
```

--------------------------------

### Setting Up Virtual Environment with venv - Bash

Source: https://github.com/simonw/llm/blob/main/docs/contributing.md

Initializes a Python virtual environment named 'venv' in the 'llm' directory and activates it. This isolates project dependencies, preventing conflicts with system-wide packages.

```bash
cd llm
python -m venv venv
source venv/bin/activate
```

--------------------------------

### Advanced llm embed-multi Usage with Multiple Options

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

This comprehensive example showcases the use of `llm embed-multi` with several advanced options. It demonstrates embedding data from a JSON file into a specific database, using a particular model, adding a prefix to IDs, and storing the original content, illustrating a typical production-ready command.

```bash
llm embed-multi items mydata.json \
  -d docs.db \
  -m 3-small \
  --prefix my-items/ \
  --store
```

--------------------------------

### Display detailed options for LLM models using `llm models --options`

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Add the `--options` flag to the `llm models` command to view comprehensive documentation for the parameters and features supported by each listed model, including temperature, max_tokens, attachment types, and API keys.

```bash
llm models --options
```

```APIDOC
OpenAI Chat: gpt-4o (aliases: 4o)
  Options:
    temperature: float
      What sampling temperature to use, between 0 and 2. Higher values like
      0.8 will make the output more random, while lower values like 0.2 will
      make it more focused and deterministic.
    max_tokens: int
      Maximum number of tokens to generate.
    top_p: float
      An alternative to sampling with temperature, called nucleus sampling,
      where the model considers the results of the tokens with top_p
      probability mass. So 0.1 means only the tokens comprising the top 10%
      probability mass are considered. Recommended to use top_p or
      temperature but not both.
    frequency_penalty: float
      Number between -2.0 and 2.0. Positive values penalize new tokens based
      on their existing frequency in the text so far, decreasing the model's
      likelihood to repeat the same line verbatim.
    presence_penalty: float
      Number between -2.0 and 2.0. Positive values penalize new tokens based
      on whether they appear in the text so far, increasing the model's
      likelihood to talk about new topics.
    stop: str
      A string where the API will stop generating further tokens.
    logit_bias: dict, str
      Modify the likelihood of specified tokens appearing in the completion.
      Pass a JSON string like '{\"1712\":-100, \"892\":-100, \"1489\":-100}'
    seed: int
      Integer seed to attempt to sample deterministically
    json_object: boolean
      Output a valid JSON object {...}. Prompt must mention JSON.
  Attachment types:
    application/pdf, image/gif, image/jpeg, image/png, image/webp
  Features:
  - streaming
  - schemas
  - tools
  - async
  Keys:
    key: openai
    env_var: OPENAI_API_KEY
OpenAI Chat: chatgpt-4o-latest (aliases: chatgpt-4o)
  Options:
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: float
    stop: str
    logit_bias: dict, str
    seed: int
    json_object: boolean
  Attachment types:
    application/pdf, image/gif, image/jpeg, image/png, image/webp
  Features:
  - streaming
  - async
  Keys:
    key: openai
    env_var: OPENAI_API_KEY
OpenAI Chat: gpt-4o-mini (aliases: 4o-mini)
  Options:
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: float
    stop: str
    logit_bias: dict, str
    seed: int
    json_object: boolean
  Attachment types:
    application/pdf, image/gif, image/jpeg, image/png, image/webp
  Features:
  - streaming
  - schemas
  - tools
  - async
  Keys:
    key: openai
    env_var: OPENAI_API_KEY
OpenAI Chat: gpt-4o-audio-preview
  Options:
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: float
    stop: str
    logit_bias: dict, str
    seed: int
    json_object: boolean
  Attachment types:
    audio/mpeg, audio/wav
  Features:
  - streaming
  - async
  Keys:
    key: openai
    env_var: OPENAI_API_KEY
OpenAI Chat: gpt-4o-audio-preview-2024-12-17
  Options:
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: float
    stop: str
    logit_bias: dict, str
    seed: int
    json_object: boolean
  Attachment types:
    audio/mpeg, audio/wav
  Features:
  - streaming
  - async
  Keys:
    key: openai
    env_var: OPENAI_API_KEY
OpenAI Chat: gpt-4o-audio-preview-2024-10-01
  Options:
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: float
    stop: str
    logit_bias: dict, str
    seed: int
    json_object: boolean
  Attachment types:
    audio/mpeg, audio/wav
  Features:
  - streaming
  - async
  Keys:
    key: openai
    env_var: OPENAI_API_KEY
OpenAI Chat: gpt-4o-mini-audio-preview
  Options:
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
```

--------------------------------

### Get API Keys File Path (llm keys path)

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Outputs the file system path to the `keys.json` file where API keys are stored. This is useful for locating the configuration file for direct inspection or management.

```Shell
Usage: llm keys path [OPTIONS]

  Output the path to the keys.json file

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Register CLI Commands with LLM Plugin Hook

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-hooks.md

This hook allows plugins to add new commands to the `llm` command-line interface. The provided example demonstrates how to add a simple `hello-world` command that prints a message using the `click` library.

```Python
from llm import hookimpl
import click

@hookimpl
def register_commands(cli):
    @cli.command(name="hello-world")
    def hello_world():
        "Print hello world"
        click.echo("Hello world!")
```

--------------------------------

### llm fragments remove --help

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Removes a fragment alias from the LLM database. This command requires the specific alias name to be provided. An example demonstrates removing the 'docs' alias.

```APIDOC
Usage: llm fragments remove [OPTIONS] ALIAS

  Remove a fragment alias

  Example usage:

      llm fragments remove docs

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Implementing Options in Model's Execute Method

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Shows how to modify the `execute` method to retrieve and utilize the custom `length` and `delay` options from the `prompt.options` object, enabling control over generation length and simulating streaming with delays.

```python
    def execute(self, prompt, stream, response, conversation):
        text = prompt.prompt
        transitions = build_markov_table(text)
        length = prompt.options.length or 20
        for word in generate(transitions, length):
            yield word + ' '
            if prompt.options.delay:
                time.sleep(prompt.options.delay)
```

--------------------------------

### llm aliases remove --help

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Removes an existing model alias. The command requires the specific alias name to be provided as an argument. An example shows how to remove the 'turbo' alias.

```APIDOC
Usage: llm aliases remove [OPTIONS] ALIAS

  Remove an alias

  Example usage:

      $ llm aliases remove turbo

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Interactive Test of build_markov_table

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Python console session demonstrating how to call `build_markov_table` and inspect the generated transitions dictionary.

```python
>>> transitions = build_markov_table("the cat sat on the mat")
>>> transitions
{'the': ['cat', 'mat'], 'cat': ['sat'], 'sat': ['on'], 'on': ['the']}
```

--------------------------------

### Retrieving similar embeddings in plain text

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Shows how to use the `-p/--plain` option with `llm similar` to get similarity search results in a plain text format instead of JSON. This provides a more concise output for quick review.

```bash
llm similar quotations -c 'computer science' -p
```

--------------------------------

### View N Most Recent LLM Log Entries

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

Specify the number of recent log items you wish to view using the `-n` flag. For example, `-n 10` will display the ten most recent entries.

```bash
llm logs -n 10
```

--------------------------------

### Get Logs Database Path (llm logs path)

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Outputs the file system path to the `logs.db` SQLite database file where LLM interaction logs are stored. This helps in locating the database for direct access or management.

```Shell
Usage: llm logs path [OPTIONS]

  Output the path to the logs.db file

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Use a saved llm prompt template with piped content

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Applies a previously saved prompt template (`pytest`) to piped content. The template's system prompt guides the model in processing the input, such as generating pytest tests for code.

```bash
cat llm/utils.py | llm -t pytest
```

--------------------------------

### Uninstalling LLM Plugins using llm uninstall (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/plugins/installing-plugins.md

This command uninstalls a specified LLM plugin (e.g., llm-gpt4all). The -y flag is used to automatically confirm the uninstallation without requiring user interaction.

```bash
llm uninstall llm-gpt4all -y
```

--------------------------------

### Configure LLM Plugin pyproject.toml

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

TOML configuration for `llm-markov`, defining project metadata and the `llm` entry point for plugin loading.

```toml
[project]
name = "llm-markov"
version = "0.1"

[project.entry-points.llm]
markov = "llm_markov"
```

--------------------------------

### Viewing the Content of the LLM Aliases File (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/aliases.md

This command displays the raw content of the LLM aliases configuration file. It uses command substitution to dynamically get the file path and then `cat` to print its contents to the console.

```bash
cat "$(llm aliases path)"
```

--------------------------------

### Implement Asynchronous execute Method with API Key for LLM AsyncKeyModel

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

This example shows how to define the `async def execute()` method for an `llm.AsyncKeyModel`. It combines asynchronous execution with the ability to receive an API key, making it suitable for async models that require authentication.

```Python
class MyAsyncModel(llm.AsyncKeyModel):
    ...
    async def execute(
        self, prompt, stream, response, conversation=None, key=None
    ) -> AsyncGenerator[str, None]:
```

--------------------------------

### LLM YAML Template with JSON Schema

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

Shows how to embed a JSON schema using the `schema_object` key within a YAML template. This guides the language model to generate structured output that conforms to the specified schema.

```yaml
name: dogs
schema_object:
    properties:
        dogs:
            items:
                properties:
                    bio:
                        type: string
                    name:
                        type: string
                type: object
            type: array
    type: object
```

--------------------------------

### List Available LLM Prompt Templates

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Lists all prompt templates currently available to the `llm` CLI. This command is useful for discovering existing templates.

```Shell
Usage: llm templates list [OPTIONS]

  List available prompt templates

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Viewing Summaries of Logged Schemas

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

Illustrates how to list all schemas that have been automatically logged to the database by `llm`. The output provides a summary including the schema ID, a brief content summary, and usage statistics. An example output is:
```
- id: 3b7702e71da3dd791d9e17b76c88730e
  summary: |
    {items: [{name, organization, role, learned, article_headline, article_date}]}
  usage: |
    1 time, most recently 2025-02-28T04:50:02.032081+00:00
```

```bash
llm schemas
```

--------------------------------

### Start Interactive Chat Session with LLM

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm chat` command initiates an ongoing conversation with a language model directly in the terminal, offering significant performance improvements for local models by avoiding repeated loading. Users can interact, ask questions, and receive responses, with sessions automatically logged for later review.

```bash
llm chat -m mlc-chat-Llama-2-13b-chat-hf-q4f16_1
Type 'exit' or 'quit' to exit
Type '!multi' to enter multiple lines, then '!end' to finish
Type '!edit' to open your default editor and modify the prompt.
> Who are you?
Hello! I'm just an AI, here to assist you with any questions you may have.
My name is LLaMA, and I'm a large language model trained to provide helpful
and informative responses to a wide range of questions and topics. I'm here
to help you find the information you need, while ensuring a safe and
respectful conversation. Please feel free to ask me anything, and I'll do my
best to provide a helpful and accurate response.
> Tell me a joke about otters
Sure, here's a joke about otters:

Why did the otter go to the party?

Because he heard it was a "whale" of a time!

(Get it? Whale, like a big sea mammal, but also a "wild" or "fun" time.
Otters are known for their playful and social nature, so it's a lighthearted
and silly joke.)

I hope that brought a smile to your face! Do you have any other questions or
topics you'd like to discuss?
> exit
```

--------------------------------

### Example LLM Plugin Syntax Error Traceback

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

This snippet shows a typical traceback error that occurs when a broken LLM plugin, such as `llm-markov`, causes a `SyntaxError` and prevents the `llm` command from executing. This error can prevent standard uninstallation methods from working.

```bash
$ llm 'hi'
Traceback (most recent call last):
  ...
  File llm-markov/llm_markov.py", line 10
    register(Markov()):
                      ^
SyntaxError: invalid syntax
```

--------------------------------

### Generate Single Structured JSON Output with LLM Schema

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

Demonstrates how to use the `llm --schema` command-line tool to prompt a Large Language Model to generate a single JSON object conforming to a specified concise schema. This example invents a 'cool dog' with `name` (string), `age` (integer), and `one_sentence_bio` (string) fields.

```bash
llm --schema 'name, age int, one_sentence_bio' 'invent a cool dog'
```

```json
{
  "name": "Ziggy",
  "age": 4,
  "one_sentence_bio": "Ziggy is a hyper-intelligent, bioluminescent dog who loves to perform tricks in the dark and guides his owner home using his glowing fur."
}
```

--------------------------------

### List Default Options for All LLM Models

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Lists all default options currently configured for all LLM models. This command helps in reviewing the global model option settings.

```Shell
Usage: llm models options list [OPTIONS]

  List default options for all models

  Example usage:

      llm models options list

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Example JSON Output for LLM Aliases List

Source: https://github.com/simonw/llm/blob/main/docs/aliases.md

This JSON object represents a typical output from the `llm aliases list --json` command, illustrating the key-value pairs where the key is the alias and the value is the full model ID.

```json
{
    "3.5": "gpt-3.5-turbo",
    "chatgpt": "gpt-3.5-turbo",
    "4": "gpt-4",
    "gpt4": "gpt-4",
    "ada": "ada-002"
}
```

--------------------------------

### Executing Tools with Asynchronous LLM Models

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Demonstrates how to use synchronous tool functions with `llm`'s asynchronous models. It shows that `response.execute_tool_calls()`, `chain_response.text()`, and `chain_response.responses()` methods must be awaited when working with asynchronous models. The example defines a simple `upper` tool and chains prompts.

```python
import llm
model = llm.get_async_model("gpt-4.1")

def upper(string):
    "Converts string to uppercase"
    return string.upper()

chain = model.chain(
    "Convert panda to uppercase then pelican to uppercase",
    tools=[upper],
    after_call=print
)
print(await chain.text())
```

--------------------------------

### Retrieve a Stored API Key (llm keys get)

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Retrieves the value of a specific API key stored in `keys.json` by its name. This command is often used to export keys as environment variables for use in scripts or other applications.

```Shell
Usage: llm keys get [OPTIONS] NAME

  Return the value of a stored key

  Example usage:

      export OPENAI_API_KEY=$(llm keys get openai)

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Chat with a Configurable Toolbox in LLM

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Demonstrates how to initiate an interactive chat session with an LLM, pre-configured to use a specific toolbox (e.g., Datasette), allowing for continuous interaction with the toolbox.

```bash
llm chat -T 'Datasette("https://datasette.io/content")' --td
```

--------------------------------

### Filter llm similar Results by ID Prefix

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm similar` command now includes a `--prefix` option, allowing users to narrow down similarity search results to items whose IDs start with a specified string, such as a collection or category prefix.

```CLI
llm similar my-collection --prefix 'docs/'
```

--------------------------------

### Filter llm plugins by Implemented Hook

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm plugins` command now supports a `--hook <NAME>` option, enabling users to filter the list of installed plugins to show only those that implement a specific plugin hook.

```CLI
llm plugins --hook register_tool
```

--------------------------------

### Explain URL Content using Fragments

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This command utilizes the new fragments feature to provide context from a URL. It instructs LLM to explain the content of the `robots.txt` file located at the specified URL, treating the URL content as a prompt fragment.

```bash
llm -f https://llm.datasette.io/robots.txt 'explain this file'
```

--------------------------------

### Define JSON Schema for LLM Structured Output

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

A full JSON schema definition for an object with `name` (string), `age` (integer), and `one_sentence_bio` (string) fields, all marked as required. This schema guides LLM to produce structured JSON output.

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "age": {
      "type": "integer"
    },
    "one_sentence_bio": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "age",
    "one_sentence_bio"
  ]
}
```

--------------------------------

### Creating LLM Templates with --save

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

Demonstrates various ways to create and save reusable templates using the `llm` command-line tool's `--save` option. Templates can include user input placeholders (`$input`), system prompts, default models, model options, tools, Python functions, and JSON schemas. Literal dollar signs require `$$`.

```Bash
llm '$input - summarize this' --save summarize
```

```Bash
llm 'Summarize the following: ' --save summarize
```

```Bash
llm --system 'Summarize this' --save summarize
```

```Bash
llm --system 'Summarize this' --model gpt-4o --save summarize
```

```Bash
llm --system 'Speak in French' -o temperature 1.8 --save wild-french
```

```Bash
llm --system 'Estimate the cost in $$ of this: $input' --save estimate
```

```Bash
llm -T llm_time --system 'Always include the current time in the answer' --save time
```

```Bash
llm --functions 'def reverse_string(s): return s[::-1]' --system 'reverse any input' --save reverse
```

```Bash
llm -t reverse 'Hello, world!'
```

```Bash
llm --schema dog.schema.json 'invent a dog' --save dog
```

```Bash
llm --system 'write a Python function' --extract --save python-function
```

```Bash
llm -t python-function 'calculate haversine distance between two points'
```

--------------------------------

### Disabling All LLM Plugins via Environment Variable (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/plugins/installing-plugins.md

This command demonstrates how to temporarily disable all LLM plugins by setting the LLM_LOAD_PLUGINS environment variable to an empty string before executing an LLM command. This is useful for debugging or running LLM without any extensions.

```bash
LLM_LOAD_PLUGINS='' llm ...
```

--------------------------------

### llm fragments set --help

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Sets an alias for a fragment, allowing it to be referenced by a short name. The fragment content can be provided from a file path, URL, hash, or standard input. An example demonstrates setting 'mydocs' as an alias for a local Markdown file.

```APIDOC
Usage: llm fragments set [OPTIONS] ALIAS FRAGMENT

  Set an alias for a fragment

  Accepts an alias and a file path, URL, hash or '-' for stdin

  Example usage:

      llm fragments set mydocs ./docs.md

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Extracting Structured Data from Articles with LLM and Multi-Schema

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

Demonstrates how to use the `llm` command-line tool to extract structured information, specifically people's names, organizations, roles, and what was learned about them, from a web article. It pipes the content of a URL through `uvx strip-tags` to `llm`, providing a multi-line schema definition and a system prompt. The output is a JSON array of items, each representing an extracted person. An example of the JSON output is:
```json
{
  "items": [
    {
      "name": "William Alsup",
      "organization": "U.S. District Court",
      "role": "Judge",
      "learned": "He ruled that the mass firings of probationary employees were likely unlawful and criticized the authority exercised by the Office of Personnel Management.",
      "article_headline": "Judge finds mass firings of federal probationary workers were likely unlawful",
      "article_date": "2025-02-26"
    },
    {
      "name": "Everett Kelley",
      "organization": "American Federation of Government Employees",
      "role": "National President",
      "learned": "He hailed the court's decision as a victory for employees who were illegally fired.",
      "article_headline": "Judge finds mass firings of federal probationary workers were likely unlawful",
      "article_date": "2025-02-26"
    }
  ]
}
```

```bash
curl 'https://apnews.com/article/trump-federal-employees-firings-a85d1aaf1088e050d39dcf7e3664bb9f' | \
  uvx strip-tags | \
  llm --schema-multi "
name: the person's name
organization: who they represent
role: their job title or role
learned: what we learned about them from this story
article_headline: the headline of the story
article_date: the publication date in YYYY-MM-DD
" --system 'extract people mentioned in this article'
```

--------------------------------

### Use LLM GitHub Template Loader

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

This command demonstrates how to use the `llm-templates-github` plugin to load and execute a template directly from a GitHub repository. It shows piping content from a URL to `llm` and specifying the template using the `gh:` prefix, enabling seamless integration with remote template sources.

```Bash
curl -sL 'https://llm.datasette.io/' | llm -t gh:simonw/summarize
```

--------------------------------

### Extract Last Fenced Code Block from LLM Logs

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

This command extracts and returns the content of the last fenced code block found within the selected log entries. It's useful for retrieving the final code example in a multi-block response.

```bash
llm logs --extract-last
```

--------------------------------

### Enable Structured Output with JSON Schemas in LLM Models

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

To allow an LLM model to support structured output based on a JSON schema, set `support_schema = True` in the model class. The `execute()` method should then check for `prompt.schema`, which will be a Python dictionary representing the JSON schema, and use it to guide the model's response.

```python
class MyModel(llm.KeyModel):
    ...
    support_schema = True
```

--------------------------------

### Initialize LLM Log Database

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

To enable logging of prompts and responses, a SQLite database can be created at `~/.llm/log.db`. The `llm init-db` command is used to set up this database file, facilitating persistent logging.

```Shell
llm init-db
```

--------------------------------

### llm aliases set --help

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Sets an alias for a specific LLM model ID. Users can specify the model ID directly or use query strings to find a matching model. An example demonstrates setting 'mini' as an alias for 'gpt-4o-mini'.

```APIDOC
Usage: llm aliases set [OPTIONS] ALIAS [MODEL_ID]

  Set an alias for a model

  Example usage:

      llm aliases set mini gpt-4o-mini

  Alternatively you can omit the model ID and specify one or more -q options.
  The first model matching all of those query strings will be used.

      llm aliases set mini -q 4o -q mini

Options:
  -q, --query TEXT  Set alias for model matching these strings
  -h, --help        Show this message and exit.
```

--------------------------------

### Execute LLM Tool llm_version via CLI

Source: https://github.com/simonw/llm/blob/main/docs/tools.md

This snippet demonstrates how to call the `llm_version` tool from the command line using the `llm` utility. It shows the command to execute the tool and the expected output, which includes the tool call details and the LLM version number.

```bash
llm --tool llm_version "What version of LLM is this?" --td
```

--------------------------------

### Implement Asynchronous execute Method for LLM AsyncModel

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

This snippet provides an example of implementing an `async def execute()` method for an `llm.AsyncModel`. This asynchronous generator method is crucial for models that interact with remote HTTP APIs, enabling non-blocking operations and streaming responses.

```Python
from typing import AsyncGenerator
import llm

class MyAsyncModel(llm.AsyncModel):
    # This can duplicate the model_id of the sync model:
    model_id = "my-model-id"

    async def execute(
        self, prompt, stream, response, conversation=None
    ) -> AsyncGenerator[str, None]:
        if stream:
            completion = await client.chat.completions.create(
                model=self.model_id,
                messages=messages,
                stream=True,
            )
            async for chunk in completion:
                yield chunk.choices[0].delta.content
        else:
            completion = await client.chat.completions.create(
                model=self.model_name or self.model_id,
                messages=messages,
                stream=False,
            )
            if completion.choices[0].message.content is not None:
                yield completion.choices[0].message.content
```

--------------------------------

### Interacting with OpenAI Completion Models via LLM CLI

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Shows how to use the `llm` CLI with OpenAI completion models like `gpt-3.5-turbo-instruct` for direct text completion. This command sends a prompt and receives a generated response.

```bash
llm -m gpt-3.5-turbo-instruct 'Reasons to tame a wild beaver:'
```

--------------------------------

### Execute Basic Prompts with LLM Python API

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Demonstrates how to run a prompt against a specified LLM model using the Python API, including lazy loading of responses and alternative key configuration methods. It also shows how to list available models via the command line.

```python
import llm

model = llm.get_model("gpt-4o-mini")
# key= is optional, you can configure the key in other ways
response = model.prompt(
    "Five surprising names for a pet pelican",
    key="sk-..."
)
print(response.text())
```

```python
print(llm.get_model().prompt("Five surprising names for a pet pelican"))
```

```bash
llm models
```

--------------------------------

### Generate Multiple Structured JSON Outputs with LLM Multi-Schema

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

Illustrates the use of the `llm --schema-multi` command to instruct a Large Language Model to generate an array of JSON objects, each conforming to a specified schema. This example requests three 'really cool dogs', each with `name`, `age`, and `one_sentence_bio` fields, encapsulated within an 'items' array.

```bash
llm --schema-multi 'name, age int, one_sentence_bio' 'invent 3 really cool dogs'
```

```json
{
  "items": [
    {
      "name": "Echo",
      "age": 3,
      "one_sentence_bio": "Echo is a sleek, silvery-blue Siberian Husky with mesmerizing blue eyes and a talent for mimicking sounds, making him a natural entertainer."
    },
    {
      "name": "Nova",
      "age": 2,
      "one_sentence_bio": "Nova is a vibrant, spotted Dalmatian with an adventurous spirit and a knack for agility courses, always ready to leap into action."
    },
    {
      "name": "Pixel",
      "age": 4,
      "one_sentence_bio": "Pixel is a playful, tech-savvy Poodle with a rainbow-colored coat, known for her ability to interact with smart devices and her love for puzzle toys."
    }
  ]
}
```

--------------------------------

### llm tools list --help

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Displays a list of available tools that have been provided by LLM plugins. It supports outputting the list as JSON and registering custom Python functions as tools.

```APIDOC
Usage: llm tools list [OPTIONS]

  List available tools that have been provided by plugins

Options:
  --json            Output as JSON
  --functions TEXT  Python code block or file path defining functions to
                    register as tools
  -h, --help        Show this message and exit.
```

--------------------------------

### Implement execute Method with API Key Parameter in LLM KeyModel

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

This example illustrates how the `execute()` method within an `llm.KeyModel` subclass should be defined to accept an optional `key=` parameter. LLM automatically passes the resolved API key to this parameter, allowing the model to use it for external API calls.

```Python
    def execute(self, prompt, stream, response, conversation, key=None):
        # key= here will be the API key to use
```

--------------------------------

### Get Current Default Embedding Model with llm CLI

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

This command retrieves the name of the currently configured default embedding model for `llm` operations. It helps users verify which model will be used by default for `llm embed` and `llm embed-multi` commands.

```bash
llm embed-models default
```

--------------------------------

### OpenAI Chat Model: gpt-4.5-preview API Reference

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the OpenAI gpt-4.5-preview chat model, detailing its configurable options, supported attachment types, and features like streaming, schemas, tools, and async.

```APIDOC
OpenAI Chat: gpt-4.5-preview (aliases: gpt-4.5)
  Options:
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: float
    stop: str
    logit_bias: dict, str
    seed: int
    json_object: boolean
  Attachment types:
    application/pdf, image/gif, image/jpeg, image/png, image/webp
  Features:
  - streaming
  - schemas
  - tools
  - async
  Keys:
    key: openai
    env_var: OPENAI_API_KEY
```

--------------------------------

### Using OpenAI's GPT-4o Model with LLM CLI

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Demonstrates how to use the newly supported OpenAI GPT-4o model via the LLM command-line interface to generate a response.

```Shell
llm -m gpt-4o 'say hi in Spanish'
```

--------------------------------

### Python API: Get Response Token Usage Details

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

These methods on response objects allow retrieval of token usage statistics. `response.usage()` is for synchronous responses, and `await response.usage()` for asynchronous ones, both returning a `Usage` dataclass containing input and output token counts.

```APIDOC
response.usage() -> Usage(input: int, output: int, details: Optional[Any])
await response.usage() -> Usage(input: int, output: int, details: Optional[Any])
```

--------------------------------

### Python API: Get Specific Asynchronous Model

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This method allows direct retrieval of an asynchronous model by its unique identifier. It is crucial for plugins that provide `AsyncModel` subclasses, enabling applications to specifically request and utilize async-capable models.

```APIDOC
llm.get_async_model(model_id: str) -> AsyncModel
```

--------------------------------

### OpenAI Chat Model: gpt-4o-mini-audio-preview-2024-12-17

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the gpt-4o-mini-audio-preview-2024-12-17 OpenAI Chat model, detailing its configurable parameters, supported audio attachment types, and streaming/async features.

```APIDOC
Model: gpt-4o-mini-audio-preview-2024-12-17
Aliases: None
Options:
  temperature: float
  max_tokens: int
  top_p: float
  frequency_penalty: float
  presence_penalty: float
  stop: str
  logit_bias: dict, str
  seed: int
  json_object: boolean
Attachment types:
  audio/mpeg
  audio/wav
Features:
  streaming
  async
Keys:
  key: openai
  env_var: OPENAI_API_KEY
```

--------------------------------

### Execute llm prompt with streaming output

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Runs a prompt using the `llm` command-line tool. Tokens are streamed as they are generated, providing real-time feedback. This uses the default `gpt-4o-mini` model.

```bash
llm 'Ten names for cheesecakes'
```

--------------------------------

### Run Python Interpreter in LLM Environment with llm-python

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-python plugin adds a `llm python` command, which launches a Python interpreter within the same virtual environment as LLM. This is highly useful for debugging LLM-related issues or for interacting with the LLM Python API directly, especially when LLM is installed via Homebrew or pipx.

```Shell
llm python
```

--------------------------------

### Interact with OpenAI Models using LLM CLI

Source: https://github.com/simonw/llm/blob/main/README.md

Demonstrates how to set up your OpenAI API key and run various types of prompts, including basic text generation, image text extraction, and using system prompts with file input.

```bash
# Paste your OpenAI API key into this
llm keys set openai
```

```bash
# Run a prompt (with the default gpt-4o-mini model)
llm "Ten fun names for a pet pelican"
```

```bash
# Extract text from an image
llm "extract text" -a scanned-document.jpg
```

```bash
# Use a system prompt against a file
cat myfile.py | llm -s "Explain this code"
```

--------------------------------

### Handle Model-Specific Errors with llm.ModelError

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-utilities.md

The `llm.ModelError` exception is designed for models to report specific errors to the user. Raising this exception allows the LLM CLI layer to catch it and display a user-friendly error message, guiding the user on how to resolve the issue, such as missing dependencies or configuration.

```python
import llm

raise ModelError("MPT model not installed - try running 'llm mpt30b download'")
```

--------------------------------

### OpenAI Chat Model: o1-preview API Reference

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the OpenAI o1-preview chat model, outlining its options and features. This model has a specific set of features including streaming and async.

```APIDOC
OpenAI Chat: o1-preview
  Options:
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: float
    stop: str
    logit_bias: dict, str
    seed: int
    json_object: boolean
  Features:
  - streaming
  - async
  Keys:
    key: openai
    env_var: OPENAI_API_KEY
```

--------------------------------

### List OpenAI Models via llm CLI

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Lists the OpenAI models available to the user through the `llm` CLI. This command offers options to output the list as JSON and to provide an OpenAI API key directly.

```Bash
Usage: llm openai models [OPTIONS]

  List models available to you from the OpenAI API

Options:
  --json      Output as JSON
  --key TEXT  OpenAI API key
  -h, --help  Show this message and exit.
```

--------------------------------

### List Available LLM Models (llm models list)

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Displays a list of all Large Language Models configured and available for use with the `llm` tool. Options allow filtering by capabilities like async support, schema support, or tool support, and searching by query.

```Shell
Usage: llm models list [OPTIONS]

  List available models

Options:
  --options         Show options for each model, if available
  --async           List async models
  --schemas         List models that support schemas
  --tools           List models that support tools
  -q, --query TEXT  Search for models matching these strings
  -m, --model TEXT  Specific model IDs
  -h, --help        Show this message and exit.
```

--------------------------------

### Generate Fake Model Responses for Testing with llm.Response.fake()

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-utilities.md

The `llm.Response.fake()` method is a utility for generating mock response objects, primarily used in testing LLM models. It allows developers to simulate model outputs and conversations without making actual API calls, facilitating isolated and repeatable tests. This snippet includes an example of its usage in a test case and its API signature.

```python
def test_build_prompt_conversation():
    model = llm.get_model("mpt")
    conversation = model.conversation()
    conversation.responses = [
        llm.Response.fake(model, "prompt 1", "system 1", "response 1"),
        llm.Response.fake(model, "prompt 2", None, "response 2"),
        llm.Response.fake(model, "prompt 3", None, "response 3"),
    ]
    lines = model.build_prompt(llm.Prompt("prompt 4", model), conversation)
    assert lines == [
        "<|im_start|>system\nsystem 1<|im_end|>\n",
        "<|im_start|>user\nprompt 1<|im_end|>\n",
        "<|im_start|>assistant\nresponse 1<|im_end|>\n",
        "<|im_start|>user\nprompt 2<|im_end|>\n",
        "<|im_start|>assistant\nresponse 2<|im_end|>\n",
        "<|im_start|>user\nprompt 3<|im_end|>\n",
        "<|im_start|>assistant\nresponse 3<|im_end|>\n",
        "<|im_start|>user\nprompt 4<|im_end|>\n",
        "<|im_start|>assistant\n"
    ]
```

```APIDOC
Response.fake(cls, model: Model, prompt: str, system: str, response: str)
  cls: The class itself (implicit first argument)
  model: The Model instance associated with the response
  prompt: The user prompt string
  system: The system message string (can be None)
  response: The model's response string
```

--------------------------------

### Define Schema for People Extraction

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

This schema fragment defines the structure for extracting information about people, including their organization, role, what was learned about them, and details about the article they were mentioned in. It implies an array of 'items' where each item is an object conforming to the specified properties. The system prompt guides the LLM to extract people mentioned in the article.

```APIDOC
                - organization
                - role
                - learned
                - article_headline
                - article_date
                type: object
            type: array
    required:
    - items
    type: object
system: extract people mentioned in this article
```

--------------------------------

### Browsing LLM Logs with Datasette

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

Browse `llm` command logs using Datasette by piping the log database path obtained from `llm logs path` to Datasette, allowing for advanced SQL queries and visualization.

```bash
datasette "$(llm logs path)"
```

--------------------------------

### Define Basic LLM Plugin Model

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Python code for the `llm-markov` plugin, registering a `Markov` model with a placeholder `execute` method using `llm.hookimpl`.

```python
import llm

@llm.hookimpl
def register_models(register):
    register(Markov())

class Markov(llm.Model):
    model_id = "markov"

    def execute(self, prompt, stream, response, conversation):
        return ["hello world"]
```

--------------------------------

### Accessing Raw JSON Response from LLM Models (Python)

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Demonstrates how to retrieve the full, underlying JSON response from an LLM model using the `response.json()` method. This structure is specific to each model provider. The example output shows a typical JSON structure for a GPT-4o mini response, including content, creation timestamp, finish reason, model ID, object type, and detailed token usage.

```python
import llm
from pprint import pprint

model = llm.get_model("gpt-4o-mini")
response = model.prompt("3 names for an otter")
json_data = response.json()
pprint(json_data)
```

```python
{'content': 'Sure! Here are three fun names for an otter:\n' 
            '\n' 
            '1. **Splash**\n' 
            '2. **Bubbles**\n' 
            '3. **Otto** \n' 
            '\n' 
            'Feel free to mix and match or use these as inspiration!',
 'created': 1739291215,
 'finish_reason': 'stop',
 'id': 'chatcmpl-AznO31yxgBjZ4zrzBOwJvHEWgdTaf',
 'model': 'gpt-4o-mini-2024-07-18',
 'object': 'chat.completion.chunk',
 'usage': {'completion_tokens': 43,
           'completion_tokens_details': {'accepted_prediction_tokens': 0,
                                         'audio_tokens': 0,
                                         'reasoning_tokens': 0,
                                         'rejected_prediction_tokens': 0},
           'prompt_tokens': 13,
           'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0},
           'total_tokens': 56}}
```

--------------------------------

### Access Improved Help for LLM Embed Multi Command

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm embed-multi` command now provides enhanced `--help` output, offering clearer and more comprehensive documentation for its usage and options.

```Bash
llm embed-multi --help
```

--------------------------------

### OpenAI Chat Model: o1-mini API Reference

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the OpenAI o1-mini chat model, detailing its configurable options and features, similar to o1-preview.

```APIDOC
OpenAI Chat: o1-mini
  Options:
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: float
    stop: str
    logit_bias: dict, str
    seed: int
    json_object: boolean
  Features:
  - streaming
  - async
  Keys:
    key: openai
    env_var: OPENAI_API_KEY
```

--------------------------------

### OpenAI Chat Model: gpt-3.5-turbo

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the gpt-3.5-turbo OpenAI Chat model, detailing its configurable parameters and features like streaming and async.

```APIDOC
Model: gpt-3.5-turbo
Aliases: 3.5, chatgpt
Options:
  temperature: float
  max_tokens: int
  top_p: float
  frequency_penalty: float
  presence_penalty: float
  stop: str
  logit_bias: dict, str
  seed: int
  json_object: boolean
Attachment types:
  None
Features:
  streaming
  async
Keys:
  key: openai
  env_var: OPENAI_API_KEY
```

--------------------------------

### Display Toolboxes and Methods in llm tools list

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm tools list` command has been enhanced to provide a more comprehensive overview, now including details about toolboxes and the methods they contain.

```CLI
llm tools list
```

--------------------------------

### Define Schema for Extracting People from News Articles

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

Presents a multi-line schema definition using LLM's concise schema language, designed to extract specific details about individuals mentioned in news articles. The schema includes fields for `name`, `organization`, `role`, `learned` (what was learned about them), `article_headline`, and `article_date` (in YYYY-MM-DD format), with descriptions guiding the model's extraction process.

```LLM Schema DSL
name: the person's name
organization: who they represent
role: their job title or role
learned: what we learned about them from this story
article_headline: the headline of the story
article_date: the publication date in YYYY-MM-DD
```

--------------------------------

### LLM YAML Template with System Prompt

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

Shows how to define a `system` prompt in a YAML template. This provides initial instructions or context to the language model, influencing its overall behavior for subsequent user input.

```yaml
system: Summarize this
```

--------------------------------

### Run Prompt with a Specific Local GPT4All Model

Source: https://github.com/simonw/llm/blob/main/docs/other-models.md

This command demonstrates how to run a prompt using a specific model provided by the `llm-gpt4all` plugin, such as `orca-mini-3b-gguf2-q4_0`. The model will be automatically downloaded and cached upon its first use.

```bash
llm -m orca-mini-3b-gguf2-q4_0 'What is the capital of France?'
```

--------------------------------

### Passing Options via Command Line

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Demonstrates how to pass custom options to an LLM model using the `-o` or `--option` flag on the command line, specifying the option name and its value.

```bash
llm -m gpt4 "ten pet pelican names" -o temperature 1.5
```

--------------------------------

### Save LLM Templates with Default Parameters and Model

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

This command demonstrates how to save a new `llm` template named `summarize` directly from the command line. It specifies a system prompt, a default model (`gpt-4o`), and a default value for the `$voice` parameter (`GlaDOS`), ensuring consistent behavior when the template is used without explicit parameter overrides.

```Bash
llm --system 'Summarize this text in the voice of $voice' \
  --model gpt-4o -p voice GlaDOS --save summarize
```

--------------------------------

### OpenAI Chat Model: gpt-4.1-nano

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the gpt-4.1-nano OpenAI Chat model, including its configurable parameters, supported image and PDF attachment types, and features like streaming, schemas, and tools.

```APIDOC
Model: gpt-4.1-nano
Aliases: 4.1-nano
Options:
  temperature: float
  max_tokens: int
  top_p: float
  frequency_penalty: float
  presence_penalty: float
  stop: str
  logit_bias: dict, str
  seed: int
  json_object: boolean
Attachment types:
  application/pdf
  image/gif
  image/jpeg
  image/png
  image/webp
Features:
  streaming
  schemas
  tools
  async
Keys:
  key: openai
  env_var: OPENAI_API_KEY
```

--------------------------------

### OpenAI Chat Model: gpt-4-0125-preview

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the gpt-4-0125-preview OpenAI Chat model, detailing its configurable parameters and features like streaming and async.

```APIDOC
Model: gpt-4-0125-preview
Aliases: None
Options:
  temperature: float
  max_tokens: int
  top_p: float
  frequency_penalty: float
  presence_penalty: float
  stop: str
  logit_bias: dict, str
  seed: int
  json_object: boolean
Attachment types:
  None
Features:
  streaming
  async
Keys:
  key: openai
  env_var: OPENAI_API_KEY
```

--------------------------------

### Describe Git changes using llm with a system prompt

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Pipes the output of `git diff` to `llm` and uses a system prompt to instruct the model to describe the changes. This automates generating summaries of code modifications.

```bash
git diff | llm -s 'Describe these changes'
```

--------------------------------

### Manage Available LLM Models (llm models)

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Provides commands for managing and configuring available Large Language Models within the `llm` tool. This includes listing models, setting defaults, and managing model-specific options.

```Shell
Usage: llm models [OPTIONS] COMMAND [ARGS]...

  Manage available models

Options:
  -h, --help  Show this message and exit.

Commands:
  list*    List available models
  default  Show or set the default model
  options  Manage default options for models
```

--------------------------------

### Configure Capabilities for OpenAI Compatible LLM Models

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

OpenAI compatible models, configured via `extra-openai-models.yaml`, now support additional options to declare their capabilities: `supports_schema` for schema generation, `vision` for image attachments, and `audio` for audio processing.

```APIDOC
Model Configuration Options for `extra-openai-models.yaml`:
  "supports_schema": boolean (default: false) - Indicates if the model supports schema generation.
  "vision": boolean (default: false) - Indicates if the model supports vision capabilities (e.g., image attachments).
  "audio": boolean (default: false) - Indicates if the model supports audio capabilities.
```

--------------------------------

### Query LLM Prompts by Multiple Model Search Terms

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm prompt` command now includes a `-q` (query) option that can be used multiple times. This allows users to execute a prompt against the first model that matches all provided search terms, simplifying model selection when full IDs are unknown.

```Bash
llm prompt -q gpt -q 4o "What is the capital of France?"
```

--------------------------------

### OpenAI Chat Model: gpt-3.5-turbo-16k

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the gpt-3.5-turbo-16k OpenAI Chat model, detailing its configurable parameters and features like streaming and async.

```APIDOC
Model: gpt-3.5-turbo-16k
Aliases: chatgpt-16k, 3.5-16k
Options:
  temperature: float
  max_tokens: int
  top_p: float
  frequency_penalty: float
  presence_penalty: float
  stop: str
  logit_bias: dict, str
  seed: int
  json_object: boolean
Attachment types:
  None
Features:
  streaming
  async
Keys:
  key: openai
  env_var: OPENAI_API_KEY
```

--------------------------------

### Load PyPI Package Metadata as Fragments with llm-fragments-pypi

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-fragments-pypi plugin loads a PyPI package's description and metadata as fragments. This is useful for quickly querying LLM about a package's purpose, dependencies, or other relevant information directly from its PyPI entry. The command specifies the package name.

```Shell
llm -f pypi:ruff "What flake8 plugins does ruff re-implement?"
```

--------------------------------

### OpenAI Chat Model: o3-mini API Reference

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the OpenAI o3-mini chat model, including its options and features. This model supports 'reasoning_effort' and a full set of features.

```APIDOC
OpenAI Chat: o3-mini
  Options:
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: float
    stop: str
    logit_bias: dict, str
    seed: int
    json_object: boolean
    reasoning_effort: str
  Features:
  - streaming
  - schemas
  - tools
  - async
  Keys:
    key: openai
    env_var: OPENAI_API_KEY
```

--------------------------------

### Show a Specific LLM Prompt Template

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Displays the content of a specified prompt template. This allows users to review the exact text and structure of a template.

```Shell
Usage: llm templates show [OPTIONS] NAME

  Show the specified prompt template

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### OpenAI Chat Model: gpt-4-1106-preview

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the gpt-4-1106-preview OpenAI Chat model, detailing its configurable parameters and features like streaming and async.

```APIDOC
Model: gpt-4-1106-preview
Aliases: None
Options:
  temperature: float
  max_tokens: int
  top_p: float
  frequency_penalty: float
  presence_penalty: float
  stop: str
  logit_bias: dict, str
  seed: int
  json_object: boolean
Attachment types:
  None
Features:
  streaming
  async
Keys:
  key: openai
  env_var: OPENAI_API_KEY
```

--------------------------------

### Complete LLM Plugin for Markov Chain Model in Python

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

This comprehensive snippet provides the full Python code for an `llm` plugin that integrates a Markov chain model. It includes the `register_models` hook, the `build_markov_table` function for training, the `generate` function, and the `Markov` class with its `execute` method, demonstrating how to process user prompts to generate text.

```Python
import llm
import random

@llm.hookimpl
def register_models(register):
    register(Markov())

def build_markov_table(text):
    words = text.split()
    transitions = {}
    # Loop through all but the last word
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]
        transitions.setdefault(word, []).append(next_word)
    return transitions

def generate(transitions, length, start_word=None):
    all_words = list(transitions.keys())
    next_word = start_word or random.choice(all_words)
    for i in range(length):
        yield next_word
        options = transitions.get(next_word) or all_words
        next_word = random.choice(options)

class Markov(llm.Model):
    model_id = "markov"

    def execute(self, prompt, stream, response, conversation):
        text = prompt.prompt
        transitions = build_markov_table(text)
        for word in generate(transitions, 20):
            yield word + ' '
```

--------------------------------

### Manage Default Options for LLM Models

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Provides commands to manage default options for LLM models, such as listing, clearing, setting, or showing specific options. This allows for persistent configuration of model parameters.

```Shell
Usage: llm models options [OPTIONS] COMMAND [ARGS]...

  Manage default options for models

Options:
  -h, --help  Show this message and exit.

Commands:
  list*  List default options for all models
  clear  Clear default option(s) for a model
  set    Set a default option for a model
  show   List default options set for a specific model
```

--------------------------------

### Implementing Pydantic Validation and Documentation for Options

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Shows how to enhance the `Options` class using Pydantic's `Field` for descriptions and `field_validator` decorators to enforce custom validation rules for `length` (must be >= 2) and `delay` (must be between 0 and 10).

```python
    class Options(llm.Options):
        length: Optional[int] = Field(
            description="Number of words to generate",
            default=None
        )
        delay: Optional[float] = Field(
            description="Seconds to delay between each token",
            default=None
        )

        @field_validator("length")
        def validate_length(cls, length):
            if length is None:
                return None
            if length < 2:
                raise ValueError("length must be >= 2")
            return length

        @field_validator("delay")
        def validate_delay(cls, delay):
            if delay is None:
                return None
            if not 0 <= delay <= 10:
                raise ValueError("delay must be between 0 and 10")
            return delay
```

--------------------------------

### Python Function to Build Markov Table

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Python function `build_markov_table` that processes input text to create a dictionary of word transitions for a Markov chain.

```python
def build_markov_table(text):
    words = text.split()
    transitions = {}
    # Loop through all but the last word
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]
        transitions.setdefault(word, []).append(next_word)
    return transitions
```

--------------------------------

### llm fragments loaders --help

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Shows a list of fragment loaders that have been registered by various LLM plugins. These loaders define how fragments can be imported or processed.

```APIDOC
Usage: llm fragments loaders [OPTIONS]

  Show fragment loaders registered by plugins

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Configure Extra OpenAI Models with Reasoning (YAML)

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Shows how to enable a `reasoning: true` option for models in the `extra-openai-models.yaml` configuration file.

```YAML
# In extra-openai-models.yaml
model_name:
  reasoning: true
```

--------------------------------

### llm prompt Command Line Interface Reference

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Detailed reference for the `llm prompt` command, used to execute prompts with language models, including options for model selection, system prompts, attachments, and output extraction.

```bash
llm 'Capital of France?'
llm 'Capital of France?' -m gpt-4o
llm 'Capital of France?' -s 'answer in Spanish'
llm 'Extract text from this image' -a image.jpg
llm 'Describe' -a https://static.simonwillison.net/static/2024/pelicans.jpg
cat image | llm 'describe image' -a -
cat image | llm 'describe image' --at - image/jpeg
llm 'JavaScript function for reversing a string' -x
```

```APIDOC
Usage: llm prompt [OPTIONS] [PROMPT]

  Execute a prompt

Options:
  -s, --system TEXT               System prompt to use
  -m, --model TEXT                Model to use
  -d, --database FILE             Path to log database
  -q, --query TEXT                Use first model matching these strings
  -a, --attachment ATTACHMENT     Attachment path or URL or -
  --at, --attachment-type <TEXT TEXT>...
                                  Attachment with explicit mimetype,
                                  --at image.jpg image/jpeg
  -T, --tool TEXT                 Name of a tool to make available to the model
  --functions TEXT                Python code block or file path defining
                                  functions to register as tools
  --td, --tools-debug             Show full details of tool executions
  --ta, --tools-approve           Manually approve every tool execution
  --cl, --chain-limit INTEGER     How many chained tool responses to allow,
                                  default 5, set 0 for unlimited
  -o, --option <TEXT TEXT>...     key/value options for the model
  --schema TEXT                   JSON schema, filepath or ID
  --schema-multi TEXT             JSON schema to use for multiple results
  -f, --fragment TEXT             Fragment (alias, URL, hash or file path) to
                                  add to the prompt
  --sf, --system-fragment TEXT    Fragment to add to system prompt
  -t, --template TEXT             Template to use
  -p, --param <TEXT TEXT>...      Parameters for template
  --no-stream                     Do not stream output
  -n, --no-log                    Don't log to database
  --log                           Log prompt and response to the database
  -c, --continue                  Continue the most recent conversation.
  --cid, --conversation TEXT      Continue the conversation with the given ID.
  --key TEXT                      API key to use
  --save TEXT                     Save prompt with this template name
  --async                         Run prompt asynchronously
  -u, --usage                     Show token usage
  -x, --extract                   Extract first fenced code block
  --xl, --extract-last            Extract last fenced code block
  -h, --help                      Show this message and exit.
```

--------------------------------

### OpenAI Chat Model: gpt-4-turbo

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the gpt-4-turbo OpenAI Chat model, detailing its configurable parameters and features like streaming and async.

```APIDOC
Model: gpt-4-turbo
Aliases: gpt-4-turbo-preview, 4-turbo, 4t
Options:
  temperature: float
  max_tokens: int
  top_p: float
  frequency_penalty: float
  presence_penalty: float
  stop: str
  logit_bias: dict, str
  seed: int
  json_object: boolean
Attachment types:
  None
Features:
  streaming
  async
Keys:
  key: openai
  env_var: OPENAI_API_KEY
```

--------------------------------

### OpenAI Chat Model: gpt-4.1-mini

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the gpt-4.1-mini OpenAI Chat model, including its configurable parameters, supported image and PDF attachment types, and features like streaming, schemas, and tools.

```APIDOC
Model: gpt-4.1-mini
Aliases: 4.1-mini
Options:
  temperature: float
  max_tokens: int
  top_p: float
  frequency_penalty: float
  presence_penalty: float
  stop: str
  logit_bias: dict, str
  seed: int
  json_object: boolean
Attachment types:
  application/pdf
  image/gif
  image/jpeg
  image/png
  image/webp
Features:
  streaming
  schemas
  tools
  async
Keys:
  key: openai
  env_var: OPENAI_API_KEY
```

--------------------------------

### Defining Basic Model Options Class

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Illustrates the initial definition of an inner `Options` class within an LLM model, extending `llm.Options` and declaring `length` and `delay` as optional fields.

```python
class Markov(Model):
    model_id = "markov"

    class Options(llm.Options):
        length: Optional[int] = None
        delay: Optional[float] = None
```

--------------------------------

### List and Show Default LLM Model Options

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Provides commands to inspect default options. 'llm models options list' displays all default options across all models, while 'llm models options show <model_id>' shows options for a specific model.

```bash
llm models options list
```

```bash
llm models options show gpt-4o
```

--------------------------------

### Execute LLM Template with Variable and Piped HTML Input

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This command demonstrates executing a prompt template that uses a variable (`$voice`) and processes HTML content piped from a URL. It uses `curl` to fetch the content, `strip-tags` to clean HTML, and then `llm` to apply the 'summarize' template with the specified voice parameter.

```bash
curl -s 'https://til.simonwillison.net/macos/imovie-slides-and-audio' | \
  strip-tags -m | llm -t summarize -p voice GlaDOS
```

--------------------------------

### Continue Conversations with Plugin Tools in LLM

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Illustrates how to continue a conversation using tools from plugins with `llm -c` for single prompts and `llm chat -c` for interactive chat, ensuring the same tools are reused across turns.

```bash
llm -T simple_eval "12345 * 12345" --td
Tool call: simple_eval({'expression': '12345 * 12345'})
  152399025
12345 multiplied by 12345 equals 152,399,025.
llm -c "that * 6" --td
Tool call: simple_eval({'expression': '152399025 * 6'})
  914394150
152,399,025 multiplied by 6 equals 914,394,150.
llm chat -c --td
Chatting with gpt-4.1-mini
Type 'exit' or 'quit' to exit
Type '!multi' to enter multiple lines, then '!end' to finish
Type '!edit' to open your default editor and modify the prompt
> / 123
Tool call: simple_eval({'expression': '914394150 / 123'})
  7434098.780487805
914,394,150 divided by 123 is approximately 7,434,098.78.
```

--------------------------------

### Execute GitHub Template with llm-templates-github

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This command uses the `llm-templates-github` plugin to execute a template named `pelican-svg` from the `simonw/llm-templates` GitHub repository. It specifies the `o3-mini` model for the operation.

```bash
llm -t gh:simonw/pelican-svg -m o3-mini
```

--------------------------------

### Basic LLM YAML Prompt Template

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

A simple YAML template defining a `prompt` key with a placeholder `$input` for user-provided text, suitable for basic text processing tasks like summarization.

```yaml
prompt: 'Summarize this: $input'
```

--------------------------------

### OpenAI Chat Model: gpt-4-32k

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the gpt-4-32k OpenAI Chat model, detailing its configurable parameters and features like streaming and async.

```APIDOC
Model: gpt-4-32k
Aliases: 4-32k
Options:
  temperature: float
  max_tokens: int
  top_p: float
  frequency_penalty: float
  presence_penalty: float
  stop: str
  logit_bias: dict, str
  seed: int
  json_object: boolean
Attachment types:
  None
Features:
  streaming
  async
Keys:
  key: openai
  env_var: OPENAI_API_KEY
```

--------------------------------

### OpenAI Chat Model: gpt-4

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the gpt-4 OpenAI Chat model, detailing its configurable parameters and features like streaming and async.

```APIDOC
Model: gpt-4
Aliases: 4, gpt4
Options:
  temperature: float
  max_tokens: int
  top_p: float
  frequency_penalty: float
  presence_penalty: float
  stop: str
  logit_bias: dict, str
  seed: int
  json_object: boolean
Attachment types:
  None
Features:
  streaming
  async
Keys:
  key: openai
  env_var: OPENAI_API_KEY
```

--------------------------------

### Create a New LLM Prompt Template

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This command initiates the creation or editing of a new prompt template named 'summarize'. It opens the default editor to define the template's content, which is typically YAML.

```bash
llm templates edit summarize
```

--------------------------------

### Pipe Prompt to LLM Standard Input

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm` tool now supports accepting prompts directly piped to its standard input. This allows for flexible integration with other command-line tools and scripts, enabling dynamic prompt generation.

```Shell
echo "My prompt" | llm
```

--------------------------------

### Select llm model using search terms

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Uses the `-q` flag with search terms to dynamically select a model. `llm` identifies the model with the shortest ID that matches all provided lowercase substrings.

```bash
llm 'Ten names for cheesecakes' -q 4o -q mini
```

--------------------------------

### Edit LLM Template with `llm templates edit`

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

Demonstrates how to open and edit an existing template file using the `llm templates edit` command, which launches the system's default text editor for the specified template.

```bash
llm templates edit summarize
```

--------------------------------

### Access Fabric Prompt Collection with llm-templates-fabric

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-templates-fabric plugin provides access to the extensive Fabric collection of prompts. Users can pipe content into LLM and apply a specific Fabric prompt to it, such as explaining code. This integrates a rich library of curated prompts directly into the LLM workflow.

```Shell
cat setup.py | llm -t fabric:explain_code
```

--------------------------------

### Open LLM Logs Database with Datasette

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This command uses Datasette to open the LLM's `logs.db` database, which stores a history of executed prompts and responses. It dynamically retrieves the database path using `llm logs path` for cross-platform compatibility.

```bash
datasette "$(llm logs path)"
```

--------------------------------

### Using a Registered LLM Toolbox Class from CLI

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-hooks.md

This command demonstrates how to invoke a registered toolbox class, such as the `Memory` tool, directly from the LLM command-line interface. It shows the basic syntax for activating a specific tool during a chat session.

```bash
llm chat -T Memory
```

--------------------------------

### List Available OpenAI Models via LLM

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

List all OpenAI models accessible through their API, as integrated with the `llm` tool. This command fetches the latest available models.

```Shell
llm openai models
```

--------------------------------

### LLM AsyncKeyModel Class Reference

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

Documentation for the `llm.AsyncKeyModel` class, combining asynchronous capabilities with API key management for model plugins.

```APIDOC
llm.AsyncKeyModel:
  Inherits from: llm.AsyncModel, llm.KeyModel (implicitly combines features)
  Purpose: Base class for asynchronous models that require an API key.
  Methods:
    async execute(self, prompt, stream, response, conversation=None, key=None) -> AsyncGenerator[str, None]:
      Purpose: Asynchronously executes the model with the given prompt, handling API key injection.
      Parameters:
        prompt: The prompt object.
        stream: Boolean indicating if streaming is enabled.
        response: The response object.
        conversation: Optional. The conversation object.
        key (str, optional): The API key to use, automatically provided by LLM.
      Returns: AsyncGenerator yielding response content.
```

--------------------------------

### Use LLM System Prompt Shortcut

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Utilize a shorthand `-s` for the `--system` option when running `llm` commands. This simplifies specifying system-level instructions.

```Shell
llm -s
```

--------------------------------

### OpenAI Models Declare Tool and Vision Support

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Specific OpenAI models, including `gpt-4o` and `gpt-4o-mini`, now explicitly declare their support for tool usage and vision capabilities, indicating their readiness for advanced multimodal interactions.

```APIDOC
Model Capabilities:
  gpt-4o: supports_tools=True, supports_vision=True
  gpt-4o-mini: supports_tools=True, supports_vision=True
```

--------------------------------

### Show LLM Template Loaders

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Displays information about template loaders registered by plugins. This helps in understanding how `llm` discovers and loads templates from various sources.

```Shell
Usage: llm templates loaders [OPTIONS]

  Show template loaders registered by plugins

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Execute LLM Template with Piped Input

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This command demonstrates how to execute a previously defined prompt template, 'summarize', using content piped from a file. The `cat` command provides the input text to the `llm` tool, which then processes it according to the template.

```bash
cat myfile.txt | llm -t summarize
```

--------------------------------

### Manage LLM Tools

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Provides commands for managing tools that can be made available to LLMs, primarily for listing tools provided by plugins. This enables LLMs to interact with external functionalities.

```Shell
Usage: llm tools [OPTIONS] COMMAND [ARGS]...

  Manage tools that can be made available to LLMs

Options:
  -h, --help  Show this message and exit.

Commands:
  list*  List available tools that have been provided by plugins
```

--------------------------------

### Set a system prompt for llm using --system

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Sets a system prompt using the `-s` or `--system` flag. System prompts provide instructions or context to the model, influencing its overall behavior and response style.

```bash
llm 'SQL to calculate total sales by month' \
  --system 'You are an exaggerated sentient cheesecake that knows SQL and talks about cheesecake a lot'
```

--------------------------------

### Manage LLM Prompt Templates

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Provides commands for managing stored prompt templates, including listing, editing, showing, and locating the templates directory. This helps in organizing and reusing prompts.

```Shell
Usage: llm templates [OPTIONS] COMMAND [ARGS]...

  Manage stored prompt templates

Options:
  -h, --help  Show this message and exit.

Commands:
  list*    List available prompt templates
  edit     Edit the specified prompt template using the default $EDITOR
  loaders  Show template loaders registered by plugins
  path     Output the path to the templates directory
  show     Show the specified prompt template
```

--------------------------------

### Load LLM Logs into SQLite Database

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

Command to pipe LLM logs, formatted with a schema and data key, into `sqlite-utils` to create and populate a `people` table in `data.db`.

```bash
llm logs --schema t:people --data-key items --data-array | \
  sqlite-utils insert data.db people -
```

--------------------------------

### CLI: Display Model Information and Async Models

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

These CLI commands provide detailed information about available models. `llm models --options` shows various model capabilities, including attachment support, while `llm models --async` specifically lists all available asynchronous models.

```CLI
llm models --options
```

```CLI
llm models --async
```

--------------------------------

### Access `gpt-3.5-turbo-16k` Model

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `gpt-3.5-turbo-16k` model, offering a 16,000 token context length, can now be accessed using convenient short names. Users can specify this model with either `-m chatgpt-16k` or `-m 3.5-16k`.

```Shell
llm -m chatgpt-16k
llm -m 3.5-16k
```

--------------------------------

### Search Stored Fragments using llm

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Demonstrates how to search stored fragments using the '-q' option with multiple search strings. This command helps in finding specific fragments by matching keywords across their source, hash, aliases, and content, facilitating quick retrieval.

```bash
llm fragments -q pytest -q asyncio
```

--------------------------------

### Backup Logs Database (llm logs backup)

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Creates a backup of the `llm` logs database to a specified file path. This is useful for archiving logs or moving them to a different location for safekeeping.

```Shell
Usage: llm logs backup [OPTIONS] PATH

  Backup your logs database to this file

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Run Prompt with Configured OpenAI-Compatible Model

Source: https://github.com/simonw/llm/blob/main/docs/other-models.md

After configuring an OpenAI-compatible model in `extra-openai-models.yaml`, this command shows how to use it with LLM by specifying its `model_id`. This allows LLM to interact with models hosted by services like LocalAI.

```bash
llm -m orca-openai-compat 'What is the capital of France?'
```

--------------------------------

### Load Context from URL Fragment using llm

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Shows how to use the '-f' or '--fragment' option to load context directly from a URL. This allows 'llm' to process content from web resources as part of the prompt, useful for analyzing online documents or web pages.

```bash
llm -f https://llm.datasette.io/robots.txt 'explain this'
```

--------------------------------

### Generate Completion Prompt with LLM CLI

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Demonstrates how to use the `llm` command-line tool to send a completion prompt to a specified model, such as `gpt-3.5-turbo-instruct`. This is suitable for models designed to complete sentences or paragraphs rather than respond in a chat format.

```bash
llm -m gpt-3.5-turbo-instruct 'Reasons to tame a wild beaver:'
```

--------------------------------

### Show Default Options for a Specific LLM Model

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Displays the default options set for a particular LLM model. This is useful for inspecting the specific configurations applied to a chosen model.

```Shell
Usage: llm models options show [OPTIONS] MODEL

  List default options set for a specific model

  Example usage:

      llm models options show gpt-4o

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### OpenAI Chat Model: gpt-4.1

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the gpt-4.1 OpenAI Chat model, including its configurable parameters, supported image and PDF attachment types, and features like streaming, schemas, and tools.

```APIDOC
Model: gpt-4.1
Aliases: 4.1
Options:
  temperature: float
  max_tokens: int
  top_p: float
  frequency_penalty: float
  presence_penalty: float
  stop: str
  logit_bias: dict, str
  seed: int
  json_object: boolean
Attachment types:
  application/pdf
  image/gif
  image/jpeg
  image/png
  image/webp
Features:
  streaming
  schemas
  tools
  async
Keys:
  key: openai
  env_var: OPENAI_API_KEY
```

--------------------------------

### LLM Fragment Loaders Reference

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

This section provides a reference for the output of the `llm fragments loaders` command, detailing the available fragment prefixes and their functionalities. It describes how `github:` loads files from a repository and `issue:` fetches GitHub issues and comments as Markdown, along with their respective argument formats.

```APIDOC
github:
  Load files from a GitHub repository as fragments

  Argument is a GitHub repository URL or username/repository

issue:
  Fetch GitHub issue and comments as Markdown

  Argument is either "owner/repo/NUMBER"
  or "https://github.com/owner/repo/issues/NUMBER"
```

--------------------------------

### Implementing Markov Chain Generator with Python List

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

This alternative implementation of the Markov chain text generator builds and returns a list of words instead of using a generator. It serves the same purpose as the `generate` function but collects all output before returning the complete sequence of words.

```Python
def generate_list(transitions, length, start_word=None):
    all_words = list(transitions.keys())
    next_word = start_word or random.choice(all_words)
    output = []
    for i in range(length):
        output.append(next_word)
        options = transitions.get(next_word) or all_words
        next_word = random.choice(options)
    return output
```

--------------------------------

### Searching for similar binary content

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Shows how to find images similar to an input image using `llm similar` with `-i filename` and the `--binary` option for models like CLIP. This enables visual similarity searches based on image embeddings.

```bash
llm similar photos -i image.jpg --binary
```

--------------------------------

### Manage LLM Schemas and DSL (CLI)

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Commands for listing, showing, and debugging the concise schema language (DSL) used within the LLM project.

```Bash
llm schemas list
```

```Bash
llm schemas show
```

```Bash
llm schemas dsl
```

--------------------------------

### Python API: Model Key Handling

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Plugins can now subclass `llm.KeyModel` and `llm.AsyncKeyModel` to accept API keys. The key is passed as a `key` parameter to their `.execute()` methods, enabling users to pass keys via `model.prompt(..., key=)`.

```APIDOC
llm.KeyModel:
  Base class for synchronous models requiring an API key.
  Methods:
    execute(prompt: str, key: str = None, **kwargs)
      prompt: The input prompt string.
      key: The API key for the model.

llm.AsyncKeyModel:
  Base class for asynchronous models requiring an API key.
  Methods:
    execute(prompt: str, key: str = None, **kwargs)
      prompt: The input prompt string.
      key: The API key for the model.

llm.Model.prompt:
  Method to prompt a model, now accepting an optional API key.
  Parameters:
    ...
    key: str (optional) - The API key to use for the prompt.
```

--------------------------------

### Interactive Shell Command Completion with llm-cmd-comp

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-cmd-comp plugin provides a key binding for the shell that launches an interactive chat to help build a command. Once the command is ready, hitting enter inserts it directly into the shell's command line, ready for execution. This offers an intuitive way to construct complex commands.

```Shell
(Shell key binding to launch llm-cmd-comp chat)
```

--------------------------------

### Retrieving Log Probabilities from OpenAI Completion Models

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Illustrates how to use the `-o logprobs` option with OpenAI completion models to include token log probabilities in the response. This provides detailed insights into the model's decision-making process.

```bash
llm -m gpt-3.5-turbo-instruct 'Say hello succinctly' -o logprobs 3
```

--------------------------------

### Debugging OpenAI API Responses (Streaming) - Bash

Source: https://github.com/simonw/llm/blob/main/docs/contributing.md

Sets an environment variable to enable detailed logging of OpenAI API requests and responses to the console. This command demonstrates a call to the 'chatgpt' model with a specific prompt, showing the streaming output.

```bash
LLM_OPENAI_SHOW_RESPONSES=1 llm -m chatgpt 'three word slogan for an an otter-run bakery'
```

--------------------------------

### Call Pre-registered LLM Tools from Command Line

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Illustrates how to invoke Python functions that have been previously registered as LLM tools using the `register_tools()` plugin hook. This allows for convenient execution of predefined tools directly from the command line.

```bash
llm -T multiply 'What is 34234 * 213345?'
```

--------------------------------

### Generate Plain Text Output for LLM Similar Commands

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm similar` command now supports a `--plain` (or `-p`) option to produce more human-readable output, contrasting with the default JSON format. This is useful for quick inspections.

```Bash
llm similar --plain
```

--------------------------------

### Implementing Markov Chain Generator with Python Yield

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

This snippet demonstrates how to create a Markov chain text generator using a Python generator function. It takes a `transitions` dictionary, desired `length`, and an optional `start_word`. The function yields words one by one, picking the next word randomly from available transitions or falling back to a random word from all words.

```Python
def generate(transitions, length, start_word=None):
    all_words = list(transitions.keys())
    next_word = start_word or random.choice(all_words)
    for i in range(length):
        yield next_word
        options = transitions.get(next_word) or all_words
        next_word = random.choice(options)
```

--------------------------------

### OpenAI Chat Model: o4-mini API Reference

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the OpenAI o4-mini chat model, detailing its configurable options, supported attachment types, and features, including 'reasoning_effort'.

```APIDOC
OpenAI Chat: o4-mini
  Options:
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: float
    stop: str
    logit_bias: dict, str
    seed: int
    json_object: boolean
    reasoning_effort: str
  Attachment types:
    application/pdf, image/gif, image/jpeg, image/png, image/webp
  Features:
  - streaming
  - schemas
  - tools
  - async
  Keys:
    key: openai
    env_var: OPENAI_API_KEY
```

--------------------------------

### List llm Collections

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Displays a list of all available `llm` collections. This command supports specifying a custom database path and can output the list in JSON format for programmatic use.

```Bash
Usage: llm collections list [OPTIONS]

  View a list of collections

Options:
  -d, --database FILE  Path to embeddings database
  --json               Output as JSON
  -h, --help           Show this message and exit.
```

--------------------------------

### Run LLM Prompt with Model Alias

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Demonstrates how to run a prompt using the LLM CLI, specifying a model using its alias (e.g., '4o' for 'gpt-4o'). The prompt text is passed as a string.

```bash
llm -m 4o \
  'As many names for cheesecakes as you can think of, with detailed descriptions'
```

--------------------------------

### Manage LLM Interaction Logs (llm logs)

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Provides a suite of commands for exploring, managing, and configuring the logging of prompts and responses from LLM interactions. It allows users to control logging status, backup logs, and list entries.

```Shell
Usage: llm logs [OPTIONS] COMMAND [ARGS]...

  Tools for exploring logged prompts and responses

Options:
  -h, --help  Show this message and exit.

Commands:
  list*   Show logged prompts and their responses
  backup  Backup your logs database to this file
  off     Turn off logging for all prompts
  on      Turn on logging for all prompts
  path    Output the path to the logs.db file
  status  Show current status of database logging
```

--------------------------------

### Piping File Content to llm with a Prompt

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This command demonstrates how to pipe the content of a file, such as a Python script, directly into the `llm` tool while simultaneously providing a prompt for explanation. This functionality works even with models that do not natively support system prompts.

```bash
cat script.py | llm 'explain this code'
```

--------------------------------

### Manage LLM Schemas

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Provides commands for managing stored schemas, including listing, showing, and converting LLM's schema DSL to JSON schema. This facilitates structured data interaction with LLMs.

```Shell
Usage: llm schemas [OPTIONS] COMMAND [ARGS]...

  Manage stored schemas

Options:
  -h, --help  Show this message and exit.

Commands:
  list*  List stored schemas
  dsl    Convert LLM's schema DSL to a JSON schema
  show   Show a stored schema
```

--------------------------------

### Load Templates from GitHub with llm-templates-github

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-templates-github plugin allows users to load templates directly from GitHub repositories. This simplifies the process of reusing and sharing prompts and templates across different projects or with other users. The command specifies the GitHub user and repository name.

```Shell
llm -t gh:simonw/pelican-svg
```

--------------------------------

### Using GPT-4 Turbo with LLM Chat CLI

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Demonstrates how to interact with the new GPT-4 Turbo model using the `llm chat` command-line interface. Users can specify the model by its full name or a short alias.

```bash
llm chat -m gpt-4-turbo
```

```bash
llm chat -m 4t
```

--------------------------------

### Enabling Full OpenAI HTTP Response Display

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Explains the `LLM_OPENAI_SHOW_RESPONSES` environment variable. Setting this variable to `1` enables the display of the complete HTTP response from OpenAI-compatible APIs, which is useful for debugging and detailed inspection.

```bash
export LLM_OPENAI_SHOW_RESPONSES=1
```

--------------------------------

### List Stored API Keys (llm keys list)

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Displays a list of all API keys currently stored by the `llm` tool. This command provides an overview of available keys managed by the application.

```Shell
Usage: llm keys list [OPTIONS]

  List names of all stored keys

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Debugging OpenAI API Responses with LLM Environment Variable

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Explains how to use the `LLM_OPENAI_SHOW_RESPONSES=1` environment variable to enable more detailed HTTP request and response information for OpenAI and compatible APIs, aiding in debugging.

```Shell
LLM_OPENAI_SHOW_RESPONSES=1 llm chat
```

--------------------------------

### OpenAI Chat Model: gpt-4-turbo-2024-04-09

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the gpt-4-turbo-2024-04-09 OpenAI Chat model, detailing its configurable parameters and features like streaming and async.

```APIDOC
Model: gpt-4-turbo-2024-04-09
Aliases: None
Options:
  temperature: float
  max_tokens: int
  top_p: float
  frequency_penalty: float
  presence_penalty: float
  stop: str
  logit_bias: dict, str
  seed: int
  json_object: boolean
Attachment types:
  None
Features:
  streaming
  async
Keys:
  key: openai
  env_var: OPENAI_API_KEY
```

--------------------------------

### Count OpenAI Tokens with ttok

Source: https://github.com/simonw/llm/blob/main/docs/related-tools.md

Shows how to use `ttok` to count the number of OpenAI tokens in a text file, useful for checking against token limits before processing with an LLM.

```bash
cat my-file.txt | ttok
```

--------------------------------

### OpenAI Chat Model: gpt-4.5-preview-2025-02-27

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the gpt-4.5-preview-2025-02-27 OpenAI Chat model, detailing its configurable parameters. Attachment types information is incomplete.

```APIDOC
Model: gpt-4.5-preview-2025-02-27
Aliases: None
Options:
  temperature: float
  max_tokens: int
  top_p: float
  frequency_penalty: float
  presence_penalty: float
  stop: str
  logit_bias: dict, str
  seed: int
  json_object: boolean
Attachment types:
  (information incomplete)
Features:
  (information incomplete)
Keys:
  (information incomplete)
```

--------------------------------

### List LLM Models Supporting Schema Feature

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

Provides the command to list all available Large Language Models that are compatible with LLM's schema feature, allowing users to identify which models can produce structured JSON output based on defined schemas.

```bash
llm models --schemas
```

--------------------------------

### Generate Structured JSON Output with Concise Schema using llm

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Shows how to use LLM's custom concise schema syntax ('name,bio') with the '--schema' option to generate structured output for a single item. This simplifies schema definition for common use cases, allowing quick specification of desired fields.

```bash
llm --schema 'name,bio' 'invent a dog'
```

--------------------------------

### Pass multiple image attachments to llm using file paths

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Attaches multiple images to a single prompt using the `-a` option with file paths. This is useful for providing multiple visual contexts to multi-modal models.

```bash
llm "extract text" -a image1.jpg -a image2.jpg
```

--------------------------------

### Save Chat Persona as a Template

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Explains how to save a chat persona, including a system prompt and model, as a reusable template using the `--save` flag. This allows users to quickly return to specific chat configurations or personas.

```bash
llm --system 'You are a sentient cheesecake' -m gpt-4 --save cheesecake
```

--------------------------------

### List Available Embedding Models

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Introduces the `llm embed-models` command for listing all available embedding models.

```CLI
llm embed-models
```

--------------------------------

### llm fragments --help

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Manages reusable text snippets, referred to as fragments, that are stored in the LLM database. These fragments can be shared across multiple prompts. It provides subcommands for listing, setting, showing, removing, and viewing loaders.

```APIDOC
Usage: llm fragments [OPTIONS] COMMAND [ARGS]...

  Manage fragments that are stored in the database

  Fragments are reusable snippets of text that are shared across multiple
  prompts.

Options:
  -h, --help  Show this message and exit.

Commands:
  list*    List current fragments
  loaders  Show fragment loaders registered by plugins
  remove   Remove a fragment alias
  set      Set an alias for a fragment
  show     Display the fragment stored under an alias or hash
```

--------------------------------

### Pipe prompt content to llm via standard input

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Sends a prompt directly to the `llm` tool using standard input. The piped content is processed as the primary prompt for the language model.

```bash
echo 'Ten names for cheesecakes' | llm
```

--------------------------------

### Generate Structured JSON Output with Inline Schema using llm

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Demonstrates how to pass a full JSON schema directly to the 'llm' command using the '--schema' option to enforce structured JSON output from a language model. It specifies the model 'gpt-4o-mini' and a prompt to invent two dogs, ensuring the output adheres to the defined 'dogs' array structure.

```bash
llm --schema '{
  "type": "object",
  "properties": {
    "dogs": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "bio": {
            "type": "string"
          }
        }
      }
    }
  }
}' -m gpt-4o-mini 'invent two dogs'
```

--------------------------------

### LLM AsyncModel Class Reference

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

Documentation for the `llm.AsyncModel` class, providing an asynchronous interface for model plugins, suitable for `asyncio`.

```APIDOC
llm.AsyncModel:
  Inherits from: llm.Model
  Purpose: Base class for asynchronous model plugins.
  Properties:
    model_id (str): The identifier for the model. Can duplicate a sync model's ID.
  Methods:
    async execute(self, prompt, stream, response, conversation=None) -> AsyncGenerator[str, None]:
      Purpose: Asynchronously executes the model with the given prompt.
      Parameters:
        prompt: The prompt object.
        stream: Boolean indicating if streaming is enabled.
        response: The response object.
        conversation: Optional. The conversation object.
      Returns: AsyncGenerator yielding response content.
```

--------------------------------

### Interact with OpenAI API via llm CLI

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Provides a set of commands for direct interaction with the OpenAI API through the `llm` command-line tool. It serves as a parent command for more specific OpenAI operations, such as listing models.

```Bash
Usage: llm openai [OPTIONS] COMMAND [ARGS]...

  Commands for working directly with the OpenAI API

Options:
  -h, --help  Show this message and exit.

Commands:
  models  List models available to you from the OpenAI API
```

--------------------------------

### llm aliases list --help

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Lists all currently configured model aliases. This command provides an option to output the list in JSON format for programmatic use.

```APIDOC
Usage: llm aliases list [OPTIONS]

  List current aliases

Options:
  --json      Output as JSON
  -h, --help  Show this message and exit.
```

--------------------------------

### Pass Options to LLM Chat Session

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Illustrates how to pass model-specific options, such as `temperature`, to an `llm chat` session using the `-o` or `--option` flag. This allows for fine-tuning model behavior during the conversation.

```bash
llm chat -m gpt-4 -o temperature 0.5
```

--------------------------------

### Search for LLM models by term using `llm models -q`

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Use one or more `-q term` options to filter the list of models, showing only those that match all provided search terms.

```bash
llm models -q gpt-4o
```

```bash
llm models -q 4o -q mini
```

--------------------------------

### Load Context from File Fragment using llm

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Illustrates using the '-f' option to load context from a local file (cli.py). This enables 'llm' to incorporate local code or text files into prompts, facilitating tasks like code analysis, summarization, or creative writing based on file content.

```bash
llm -f cli.py 'a short snappy poem inspired by this code'
```

--------------------------------

### Configure Tool Support in extra-openai-models.yaml

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `supports_tools` parameter is now recognized within the `extra-openai-models.yaml` configuration file, allowing users to explicitly define tool support for custom or additional OpenAI models.

```YAML
models:
  - id: my-custom-model
    supports_tools: true
```

--------------------------------

### OpenAI Chat Model: o3 API Reference

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the OpenAI o3 chat model, detailing its configurable options, supported attachment types, and features, including 'reasoning_effort'.

```APIDOC
OpenAI Chat: o3
  Options:
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: float
    stop: str
    logit_bias: dict, str
    seed: int
    json_object: boolean
    reasoning_effort: str
  Attachment types:
    application/pdf, image/gif, image/jpeg, image/png, image/webp
  Features:
  - streaming
  - schemas
  - tools
  - async
  Keys:
    key: openai
    env_var: OPENAI_API_KEY
```

--------------------------------

### Enable Prompt Logging (llm logs on)

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Activates logging for all future `llm` prompts and their corresponding responses. This ensures that interactions are recorded in the logs database for later review.

```Shell
Usage: llm logs on [OPTIONS]

  Turn on logging for all prompts

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Group Plugin Tools with llm.Toolbox Classes

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Plugins can now organize multiple related tools that share state or configuration into 'Toolboxes' using `llm.Toolbox` classes, enhancing modularity and state management for tool collections.

```APIDOC
llm.Toolbox: A class for grouping related plugin-provided tools that share state or configuration.
```

--------------------------------

### Configure Custom SQLite Database for LLM Logs

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm prompt` command can now be configured to write its logs to a specified SQLite database file instead of the default location. This allows for custom log management and analysis.

```Bash
llm prompt -d path-to-sqlite.db
```

--------------------------------

### List Registered LLM Template Loaders

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

This command allows users to inspect the currently registered template loaders within the `llm` tool. It provides details about each loader, such as its prefix and a brief description of its functionality, which is useful for understanding how templates can be sourced from various locations.

```Bash
llm templates loaders
```

--------------------------------

### Configure Model Behavior with Options

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

See how to pass model-specific options, such as `temperature`, as keyword arguments directly to the `model.prompt()` method. This allows fine-tuning the LLM's generation parameters.

```python
model = llm.get_model()
print(model.prompt("Names for otters", temperature=0.2))
```

--------------------------------

### Displaying All LLM Logs with Tool Results

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

Display all `llm` command logs that involved at least one tool result, including those from `--functions`, by using the `--tools` flag.

```bash
llm logs --tools
```

--------------------------------

### Running Project Tests - Bash

Source: https://github.com/simonw/llm/blob/main/docs/contributing.md

Executes the project's test suite using pytest. This command verifies the functionality and correctness of the codebase, ensuring changes do not introduce regressions.

```bash
pytest
```

--------------------------------

### Markov Chain Transition Table Structure

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

JSON representation of a simple Markov chain's word transition table, mapping words to their possible next words based on an input phrase.

```json
{
  "the": ["cat", "mat"],
  "cat": ["sat"],
  "sat": ["on"],
  "on": ["the"]
}
```

--------------------------------

### Define and Use LLM Templates with Custom Named Variables

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

This snippet demonstrates how to create a custom `llm` template using YAML that accepts named variables like `$ingredients` and `$country`. It then shows how to execute this template from the command line, passing values for these variables using the `-p/--param` option. This allows for dynamic and reusable prompts.

```YAML
prompt: |
    Suggest a recipe using ingredients: $ingredients

    It should be based on cuisine from this country: $country
```

```Bash
llm -t recipe -p ingredients 'sausages, milk' -p country Germany
```

--------------------------------

### Executing LLM Templates

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

Illustrates how to execute a previously saved or external template using the `-t` or `--template` option. Templates can be referenced by name, local file path, or a URL. The `-m` option can be used to override the template's default model.

```Bash
curl -s https://example.com/ | llm -t summarize
```

```Bash
curl -s https://llm.datasette.io/en/latest/ | \
  llm -t summarize -m gpt-3.5-turbo-16k
```

```Bash
llm -t path/to/template.yaml 'extra prompt here'
```

```Bash
llm -t https://raw.githubusercontent.com/simonw/llm-templates/refs/heads/main/python-app.yaml \
  'Python app to pick a random line from a file'
```

--------------------------------

### Running Model with Options and No Streaming

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Illustrates how to use the `--no-stream` option with the LLM command, which causes the model to gather the entire response before outputting it, even if `delay` is specified.

```bash
llm -m markov "the cat sat on the mat" \
  -o length 20 -o delay 0.1 --no-stream
```

--------------------------------

### Generate Structured JSON Output from File Schema using llm

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Explains how to reference an external JSON schema file (dogs.schema.json) using the '--schema' option. This allows for more complex or reusable schemas to be defined separately and applied to 'llm' prompts, promoting modularity.

```bash
llm --schema dogs.schema.json 'invent two dogs'
```

--------------------------------

### Importing Time Module for Delay

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Adds the necessary import statement for the `time` module, which is used within the `execute` method to simulate a delay between generated tokens.

```python
import time
```

--------------------------------

### Using a Custom LLM Template Loader from CLI

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-hooks.md

This command illustrates the syntax for using a custom template loader registered via the `register_template_loaders` hook. It shows how to specify the custom prefix and template name when invoking LLM from the command line.

```bash
llm -t my-prefix:my-template
```

--------------------------------

### Support Asynchronous Tool Execution with AsyncModel

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Models that implement the `AsyncModel` interface can now execute tools asynchronously, including tool functions defined using `async def`, improving performance for long-running operations.

```APIDOC
AsyncModel: Interface for models supporting asynchronous tool execution.
async def tool_function(...): # Example of an async tool function
```

--------------------------------

### Generate Structured Output Using LLM with JSON Schema

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

Command demonstrating how to pass an inline JSON schema to the `llm` tool using the `--schema` option to generate structured output based on a prompt.

```bash
llm --schema '{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "age": {
      "type": "integer"
    },
    "one_sentence_bio": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "age",
    "one_sentence_bio"
  ]
}' 'a surprising dog'
```

--------------------------------

### Access Fast Groq Hosted Models via llm-groq Plugin

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-groq plugin, by Moritz Angermann, provides access to fast models hosted by Groq. It allows LLM to leverage Groq's high-performance inference capabilities.

```APIDOC
Plugin: llm-groq
  API Provider: Groq
  Models Supported: Fast models hosted by Groq
  Purpose: Provides access to Groq's high-speed inference models.
```

--------------------------------

### Output Path to LLM Templates Directory

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Prints the file system path where `llm` prompt templates are stored. This is useful for direct file system access or scripting.

```Shell
Usage: llm templates path [OPTIONS]

  Output the path to the templates directory

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Combine piped content with command-line arguments in llm

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Combines content piped from standard input with additional command-line arguments. The piped text forms the initial part of the prompt, followed by the arguments.

```bash
cat myscript.py | llm 'explain this code'
```

--------------------------------

### Save and Reuse Schemas as Prompt Templates in llm

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Demonstrates how to save a JSON schema as a named prompt template using '--save' and then reuse it with the '-t' option. This streamlines workflows by allowing frequently used schemas to be quickly applied without retyping or re-referencing file paths, enhancing efficiency.

```bash
llm --schema dogs.schema.json --save dogs
# Then to use it:
llm -t dogs 'invent two dogs'
```

--------------------------------

### Viewing Recent LLM Logs

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Shows the command to retrieve the most recent log entry from the LLM database, which includes details about model execution and used options.

```bash
llm logs -n 1
```

--------------------------------

### Listing Available OpenAI Language Models in LLM

Source: https://github.com/simonw/llm/blob/main/docs/openai-models.md

This output shows a comprehensive list of OpenAI language models supported by the LLM tool, categorized by type (Chat, Completion) and including their aliases. This helps users identify which models are available for use with LLM.

```bash
OpenAI Chat: gpt-4o (aliases: 4o)
OpenAI Chat: chatgpt-4o-latest (aliases: chatgpt-4o)
OpenAI Chat: gpt-4o-mini (aliases: 4o-mini)
OpenAI Chat: gpt-4o-audio-preview
OpenAI Chat: gpt-4o-audio-preview-2024-12-17
OpenAI Chat: gpt-4o-audio-preview-2024-10-01
OpenAI Chat: gpt-4o-mini-audio-preview
OpenAI Chat: gpt-4o-mini-audio-preview-2024-12-17
OpenAI Chat: gpt-4.1 (aliases: 4.1)
OpenAI Chat: gpt-4.1-mini (aliases: 4.1-mini)
OpenAI Chat: gpt-4.1-nano (aliases: 4.1-nano)
OpenAI Chat: gpt-3.5-turbo (aliases: 3.5, chatgpt)
OpenAI Chat: gpt-3.5-turbo-16k (aliases: chatgpt-16k, 3.5-16k)
OpenAI Chat: gpt-4 (aliases: 4, gpt4)
OpenAI Chat: gpt-4-32k (aliases: 4-32k)
OpenAI Chat: gpt-4-1106-preview
OpenAI Chat: gpt-4-0125-preview
OpenAI Chat: gpt-4-turbo-2024-04-09
OpenAI Chat: gpt-4-turbo (aliases: gpt-4-turbo-preview, 4-turbo, 4t)
OpenAI Chat: gpt-4.5-preview-2025-02-27
OpenAI Chat: gpt-4.5-preview (aliases: gpt-4.5)
OpenAI Chat: o1
OpenAI Chat: o1-2024-12-17
OpenAI Chat: o1-preview
OpenAI Chat: o1-mini
OpenAI Chat: o3-mini
OpenAI Chat: o3
OpenAI Chat: o4-mini
OpenAI Completion: gpt-3.5-turbo-instruct (aliases: 3.5-instruct, chatgpt-instruct)
```

--------------------------------

### Running Prompt with Custom OpenAI Model in LLM

Source: https://github.com/simonw/llm/blob/main/docs/openai-models.md

This command demonstrates how to use a newly configured custom OpenAI model (aliased as `0613`) to run a prompt. It sends the specified text to the model and expects a response, confirming the custom model's availability and functionality.

```bash
llm -m 0613 'What is the capital of France?'
```

--------------------------------

### Embed Binary Data from Standard Input using llm embed

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Illustrates how to pipe binary data from standard input to `llm embed` using the `--binary` and `-i -` options. This provides flexibility for processing data streams.

```bash
cat image.jpg | llm embed --binary -m clip -i -
```

--------------------------------

### Browsing LLM Logs by Schema

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

View `llm` command responses that used a specified schema using the `--schema` option. This can be combined with data extraction options like `--data` for more detailed analysis.

```bash
llm logs --schema 'name, age int, bio'
```

--------------------------------

### Turn On LLM Logging by Default

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

Execute this command to re-enable logging for all `llm` prompts and responses. All future interactions will be recorded in the SQLite database.

```bash
llm logs on
```

--------------------------------

### List Logged Prompts and Responses (llm logs list)

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Displays a detailed list of logged prompts and their responses, offering extensive filtering and output options. Users can filter by count, model, query, schema, and output format (JSON, YAML) to find specific interactions.

```Shell
Usage: llm logs list [OPTIONS]

  Show logged prompts and their responses

Options:
  -n, --count INTEGER         Number of entries to show - defaults to 3, use 0
                              for all
  -d, --database FILE         Path to log database
  -m, --model TEXT            Filter by model or model alias
  -q, --query TEXT            Search for logs matching this string
  -f, --fragment TEXT         Filter for prompts using these fragments
  -T, --tool TEXT             Filter for prompts with results from these tools
  --tools                     Filter for prompts with results from any tools
  --schema TEXT               JSON schema, filepath or ID
  --schema-multi TEXT         JSON schema used for multiple results
  --data                      Output newline-delimited JSON data for schema
  --data-array                Output JSON array of data for schema
  --data-key TEXT             Return JSON objects from array in this key
  --data-ids                  Attach corresponding IDs to JSON objects
  -t, --truncate              Truncate long strings in output
  -s, --short                 Shorter YAML output with truncated prompts
  -u, --usage                 Include token usage
  -r, --response              Just output the last response
  -x, --extract               Extract first fenced code block
  --xl, --extract-last        Extract last fenced code block
  -c, --current               Show logs from the current conversation
  --cid, --conversation TEXT  Show logs for this conversation ID
  --id-gt TEXT                Return responses with ID > this
  --id-gte TEXT               Return responses with ID >= this
  --json                      Output logs as JSON
  -e, --expand                Expand fragments to show their content
  -h, --help                  Show this message and exit.
```

--------------------------------

### Searching for similar embeddings from standard input

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Illustrates how to pipe text to standard input and use `-i -` with `llm similar` for similarity search. This allows for dynamic input directly from other commands or scripts.

```bash
echo 'computer science' | llm similar quotations -i -
```

--------------------------------

### Updating OpenAI API Recordings and Snapshots - Bash

Source: https://github.com/simonw/llm/blob/main/docs/contributing.md

Runs pytest with specific environment variables and flags to record new OpenAI API responses and update test snapshots. This is crucial when adding new API-calling tests or modifying existing ones, requiring `pytest-recording` and `syrupy`.

```bash
PYTEST_OPENAI_API_KEY="$(llm keys get openai)" pytest --record-mode once --snapshot-update
```

--------------------------------

### List LLM Models Supporting Schemas (CLI)

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Command to display a list of models that have integrated schema support, useful for identifying compatible models.

```Bash
llm models --schemas
```

--------------------------------

### View Shortened LLM Logs in YAML Mode

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

Use the `--short` flag to display logs in a concise YAML format. This mode truncates prompts and omits responses, providing a compact overview of recent interactions.

```bash
llm logs -n 2 --short
```

--------------------------------

### Set model-specific options for llm prompts

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Passes specific options, like `temperature`, to the model using the `-o` or `--option` flag. This allows fine-tuning model behavior for a given prompt.

```bash
llm 'Ten names for cheesecakes' -o temperature 1.5
```

--------------------------------

### Configure Editor for LLM Templates using `EDITOR`

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

Shows how to set the `EDITOR` environment variable to specify a custom editor (e.g., VS Code) that `llm` commands will use when opening files for editing.

```bash
export EDITOR="code -w"
```

--------------------------------

### Calculate and Store Embeddings via CLI

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Explains the `llm embed` command used to calculate embeddings for content and either return them to the console or store them in a SQLite database.

```CLI
llm embed <content>
```

--------------------------------

### LLM YAML Template with Fragments

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

Illustrates how to include external content as `fragments` or `system_fragments` in a template. These can be referenced by URL, file path, or hash, allowing for dynamic content injection.

```yaml
fragments:
- https://example.com/robots.txt
- /path/to/file.txt
- 993fd38d898d2b59fd2d16c811da5bdac658faa34f0f4d411edde7c17ebb0680
system_fragments:
- https://example.com/systm-prompt.txt
```

--------------------------------

### llm aliases path --help

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Outputs the file path to the `aliases.json` file, which stores all configured model aliases. This is useful for directly accessing or inspecting the alias configuration.

```APIDOC
Usage: llm aliases path [OPTIONS]

  Output the path to the aliases.json file

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### View Shortened LLM Logs with Token Usage Information

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

This command extends the `--short` mode by including token usage details for each log entry. The `--usage` flag adds input and output token counts to the YAML output.

```bash
llm logs -n 1 --short --usage
```

--------------------------------

### Show or Set Default LLM Model

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Displays or configures the default LLM model used by the `llm` CLI. Users can view the current default or set a new one using this command.

```Shell
Usage: llm models default [OPTIONS] [MODEL]

  Show or set the default model

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Generate and Execute Shell Commands with llm-cmd

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-cmd plugin accepts a natural language prompt for a shell command. It generates the command, populates it in the user's shell for review and editing, and allows execution or cancellation. This streamlines command-line interaction by leveraging LLM for command generation.

```Shell
llm-cmd (followed by a prompt, e.g., 'create a directory named my_project')
```

--------------------------------

### Enable Tool Usage in llm chat Sessions

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm chat` command now supports integrating tools into interactive chat sessions. Users can specify tools using the `--tool` argument or define functions with `--functions`.

```CLI
llm chat --tool <tool_name>
llm chat --functions <function_definition>
```

--------------------------------

### Create Embeddings from Python Symbols with Symbex and LLM

Source: https://github.com/simonw/llm/blob/main/docs/related-tools.md

Shows how to use `symbex` to export all Python symbols in a newline-delimited format, which is then piped to `llm embed-multi` to create and store embeddings in a database.

```bash
symbex '*' '*:*' --nl | \
  llm embed-multi symbols - \
  --format nl --database embeddings.db --store
```

--------------------------------

### llm chat Command Line Interface Reference

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Reference for the `llm chat` command, enabling ongoing conversations with language models, with options for continuing conversations, system prompts, and tool integration.

```APIDOC
Usage: llm chat [OPTIONS]

  Hold an ongoing chat with a model.

Options:
  -s, --system TEXT             System prompt to use
  -m, --model TEXT              Model to use
  -c, --continue                Continue the most recent conversation.
  --cid, --conversation TEXT    Continue the conversation with the given ID.
  -f, --fragment TEXT           Fragment (alias, URL, hash or file path) to add
                                to the prompt
  --sf, --system-fragment TEXT  Fragment to add to system prompt
  -t, --template TEXT           Template to use
  -p, --param <TEXT TEXT>...    Parameters for template
  -o, --option <TEXT TEXT>...   key/value options for the model
  -d, --database FILE           Path to log database
  --no-stream                   Do not stream output
  --key TEXT                    API key to use
  -T, --tool TEXT               Name of a tool to make available to the model
  --functions TEXT              Python code block or file path defining
                                functions to register as tools
  --td, --tools-debug           Show full details of tool executions
  --ta, --tools-approve         Manually approve every tool execution
  --cl, --chain-limit INTEGER   How many chained tool responses to allow,
                                default 5, set 0 for unlimited
  -h, --help                    Show this message and exit.
```

--------------------------------

### Run Similarity Searches on Stored Embeddings

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Describes the `llm similar` command, which enables running similarity searches against stored embeddings, using a search phrase or a previously stored vector.

```CLI
llm similar <search_phrase>
```

--------------------------------

### Integrate Shell Commands into llm Prompts

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Provides a tip for integrating shell command output directly into 'llm' prompts using '$(command)' substitution within double-quoted strings. This allows for dynamic prompt creation based on system information or other command outputs, making prompts more context-aware.

```bash
llm "Tell me about my operating system: $(uname -a)"
```

--------------------------------

### Run Python Project Tests with Pytest

Source: https://github.com/simonw/llm/blob/main/AGENTS.md

This command executes the project's automated tests using the 'pytest' framework. It verifies the functionality and correctness of the codebase, providing immediate feedback on any regressions or issues.

```bash
pytest
```

--------------------------------

### llm aliases --help

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Manages model aliases within the LLM environment. This command serves as a parent for subcommands to list, set, remove, and output the path to the aliases configuration file.

```APIDOC
Usage: llm aliases [OPTIONS] COMMAND [ARGS]...

  Manage model aliases

Options:
  -h, --help  Show this message and exit.

Commands:
  list*   List current aliases
  path    Output the path to the aliases.json file
  remove  Remove an alias
  set     Set an alias for a model
```

--------------------------------

### View All LLM Log Entries

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

To retrieve every single logged item from the database, use the `-n 0` option. This will output the complete history of prompts and responses.

```bash
llm logs -n 0
```

--------------------------------

### Support Anthropic Claude via Amazon Bedrock with llm-bedrock-anthropic

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-bedrock-anthropic plugin, by Sean Blakey, adds support for Claude and Claude Instant by Anthropic via Amazon Bedrock. It allows LLM to access Anthropic models through AWS Bedrock.

```APIDOC
Plugin: llm-bedrock-anthropic
  API Provider: Amazon Bedrock (for Anthropic models)
  Models Supported: Claude, Claude Instant by Anthropic
  Purpose: Integrates Anthropic's Claude models via Amazon Bedrock.
```

--------------------------------

### Process URL Content with Fabric Template

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This command demonstrates using the `llm-templates-fabric` plugin to process content from a URL. It pipes the output of `curl` into `llm`, which then applies the `extract_main_idea` template from the Fabric collection.

```bash
curl https://simonwillison.net/2025/Apr/6/only-miffy/ | \n  llm -t f:extract_main_idea
```

--------------------------------

### List Stored LLM Schemas

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Lists all stored schemas, with options to filter by database, query, output full contents, or format as JSON/newline-delimited JSON. This command is essential for schema discovery and inspection.

```Shell
Usage: llm schemas list [OPTIONS]

  List stored schemas

Options:
  -d, --database FILE  Path to log database
  -q, --query TEXT     Search for schemas matching this string
  --full               Output full schema contents
  --json               Output as JSON
  --nl                 Output as newline-delimited JSON
  -h, --help           Show this message and exit.
```

--------------------------------

### Approve Tool Calls Interactively with LLM

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Illustrates the use of the `--ta` (or `--tools-approve`) option to prompt for interactive approval before a tool call is executed by the LLM, providing a safety mechanism.

```bash
llm --functions '
def multiply(x: int, y: int) -> int:
    """Multiply two numbers."""
    return x * y
' 'what is 34234 * 213345' --ta
```

--------------------------------

### OpenAI Chat Model: o1 API Reference

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the OpenAI o1 chat model, including its options, attachment types, and features. This model includes the 'reasoning_effort' option.

```APIDOC
OpenAI Chat: o1
  Options:
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: float
    stop: str
    logit_bias: dict, str
    seed: int
    json_object: boolean
    reasoning_effort: str
  Attachment types:
    application/pdf, image/gif, image/jpeg, image/png, image/webp
  Features:
  - schemas
  - tools
  - async
  Keys:
    key: openai
    env_var: OPENAI_API_KEY
```

--------------------------------

### Quick Schema Definition using LLM's DSL

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Discover LLM's `schema_dsl()` function for quickly defining simple JSON schemas using a concise string syntax. This is ideal for rapid prototyping and straightforward output requirements.

```python
print(model.prompt(
    "Describe a nice dog with a surprising name",
    schema=llm.schema_dsl("name, age int, bio")
))
```

--------------------------------

### Setting OpenAI API Key for LLM

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Instructions on how to set the OpenAI API key using the `llm keys set` command to access OpenAI's `ada-002` embedding model.

```CLI
llm keys set openai
```

--------------------------------

### Alias and Reuse Fragments using llm

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Explains how to set an alias for a fragment using 'llm fragments set' and then reference it by its alias with the '-f' option. This simplifies repeated use of common fragments, avoiding the need to specify the full path or URL each time, improving command brevity.

```bash
llm fragments set cli cli.py
# Then
llm -f cli 'explain this code'
```

--------------------------------

### Invoking a Registered Fragment Loader via CLI

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-hooks.md

This Bash command demonstrates how to call a previously registered fragment loader from the command line. The `-f` flag is used, followed by the registered prefix (`my-fragments`) and the argument to be passed to the loader.

```bash
llm -f my-fragments:argument
```

--------------------------------

### Backing Up LLM Log Database

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

Backup the `llm` command logs database to another file using the `llm logs backup` command. This process utilizes SQLite's `VACUUM INTO` for efficient database copying.

```bash
llm logs backup /tmp/backup.db
```

--------------------------------

### List Stored Fragments using llm

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Shows the 'llm fragments' command, which lists all fragments that have been stored. This command is useful for managing and reviewing available fragments, providing an overview of saved contextual data.

```bash
llm fragments
```

--------------------------------

### LLM CLI Schema Specification Options

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

Documentation for the `--schema` option in the `llm` command-line interface, detailing various ways to specify a schema definition for prompts and logged responses.

```APIDOC
LLM CLI --schema Option:
  Purpose: Specifies a schema definition for running prompts and exploring logged responses.
  Accepted Forms:
    - A string providing a JSON schema:
      Example: --schema '{"type": "object", ...}'
    - A condensed schema definition:
      Example: --schema 'name,age int'
    - The name or path of a file on disk containing a JSON schema:
      Example: --schema dogs.schema.json
    - The hexadecimal ID of a previously logged schema:
      Example: --schema 520f7aabb121afd14d0c6c237b39ba2d (IDs found using 'llm schemas' command)
    - A schema that has been saved in a template:
      Example: --schema t:name-of-template (see schemas-reusable)
```

--------------------------------

### Load GitHub Repositories and Issues as Fragments with llm-fragments-github

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-fragments-github plugin enables loading entire GitHub repositories as fragments for LLM, allowing users to prompt against the codebase. It also supports fetching specific GitHub issue threads as Markdown, making it useful for summarizing discussions or understanding context from issues.

```Shell
llm -f github:simonw/files-to-prompt 'explain this code'
```

```Shell
llm -f issue:https://github.com/simonw/llm-fragments-github/issues/3
```

--------------------------------

### Displaying Specific LLM Fragment Content

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

Display the full content for a specific fragment hash ID or alias using the `llm fragments show` command.

```bash
llm fragments show 993fd38d898d2b59fd2d16c811da5bdac658faa34f0f4d411edde7c17ebb0680
```

--------------------------------

### Add Amazon Bedrock Nova Support with llm-bedrock Plugin

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-bedrock plugin adds support for Nova by Amazon via Amazon Bedrock. It enables LLM to interact with Amazon's foundational models through the Bedrock service.

```APIDOC
Plugin: llm-bedrock
  API Provider: Amazon Bedrock
  Models Supported: Nova by Amazon
  Purpose: Provides support for Amazon's Nova model via Bedrock.
```

--------------------------------

### Transform JSON Data with Generated JQ Programs using llm-jq

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-jq plugin allows users to pipe in JSON data and provide a natural language prompt describing a `jq` program. LLM then generates the `jq` program, which is executed against the input JSON data. This automates JSON manipulation based on natural language instructions.

```Shell
cat data.json | llm -p "generate jq to extract names" | jq -f -
```

--------------------------------

### LLM KeyModel Class Reference

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

Documentation for the `llm.KeyModel` class, used for models requiring API keys. It inherits from `llm.Model` and adds key management capabilities.

```APIDOC
llm.KeyModel:
  Inherits from: llm.Model
  Purpose: Base class for models that require an API key.
  Properties:
    needs_key (str): Required. A string identifier for the API key in the key registry (e.g., "hosted").
    key_env_var (str): Optional. The name of the environment variable to check for the API key (e.g., "HOSTED_API_KEY").
  Methods:
    execute(self, prompt, stream, response, conversation, key=None):
      Purpose: Executes the model with the given prompt, handling API key injection.
      Parameters:
        prompt: The prompt object.
        stream: Boolean indicating if streaming is enabled.
        response: The response object.
        conversation: Optional. The conversation object.
        key (str, optional): The API key to use, automatically provided by LLM from environment, registry, or CLI.
      Returns: Generator yielding response content.
```

--------------------------------

### Set System Prompt for LLM Chat

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Demonstrates how to provide a system prompt to an `llm chat` conversation using the `-s` flag. A system prompt helps define the model's persona or instructions for the entire chat session.

```bash
llm chat -m gpt-4 -s 'You are a sentient cheesecake'
```

--------------------------------

### CLI: Enhanced Model Search and Listing

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm models` and `llm embed-models` commands now support multiple `-q` search fragments for combined queries. Additionally, `llm models` now displays the current default model at the bottom of its output.

```Shell
llm models -q gemini -q exp
llm embed-models -q "text-embedding" -q "large"
llm models
```

--------------------------------

### Perform Bulk Embeddings from Various Sources

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Details the `llm embed-multi` command for running bulk embeddings from multiple strings, supporting input from CSV, TSV, JSON files, SQLite databases, or filesystem scans.

```CLI
llm embed-multi --files <path> --format <format>
```

--------------------------------

### Chaining Prompts in LLM Conversations with Tools

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Shows how to use the `conversation.chain()` method multiple times within a tool-enabled conversation. This allows for complex, multi-step interactions where the model can leverage the provided tools across different prompts while maintaining conversational context.

```python
print(conversation.chain(
    "Convert panda to uppercase and reverse it"
).text())
print(conversation.chain(
    "Same with pangolin"
).text())
```

--------------------------------

### List All Available Embedding Models with llm CLI

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

This command lists all embedding models accessible through the `llm` CLI, including those provided by plugins. The output shows model names and their aliases, helping users identify available options for embedding operations.

```bash
llm embed-models
```

--------------------------------

### Use local file fragment in LLM prompt

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

Shows how to use a local file as a fragment in an LLM prompt. The content of the specified file will be included before the main prompt text.

```bash
llm -f setup.py 'extract the metadata'
```

--------------------------------

### Verifying Custom OpenAI Model Availability

Source: https://github.com/simonw/llm/blob/main/docs/openai-models.md

This command lists all available OpenAI models within LLM, including any custom models added via `extra-openai-models.yaml`. It's used to confirm that a newly configured model is recognized and ready for use by the LLM tool.

```bash
llm models
```

--------------------------------

### LLM YAML Template with External Tools

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

Demonstrates how to specify a list of `tools` from other plugins or toolbox specifiers within a YAML template, enabling the language model to call external functions or services.

```yaml
name: time-plus
tools:
- llm_time
- Datasette("https://example.com/timezone-lookup")
```

--------------------------------

### Obtaining Asynchronous LLM Models (Python)

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Shows how to instantiate an asynchronous LLM model using `llm.get_async_model()` for integration with Python's `asyncio` framework.

```python
import llm
model = llm.get_async_model("gpt-4o")
```

--------------------------------

### Specify Output Schemas for LLM Prompts (Python API)

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

How to pass a JSON schema dictionary or a Pydantic `BaseModel` subclass to the `model.prompt()` method in Python to enforce output structure.

```Python
model.prompt(..., schema={})
```

--------------------------------

### Prompting Asynchronous LLM Models (Python)

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Demonstrates how to send a prompt to an asynchronous LLM model using `await model.prompt(...)` and retrieve the full text response.

```python
print(await model.prompt(
    "Five surprising names for a pet pelican"
).text())
```

--------------------------------

### Pretty-Print JSON Tool Results with --tools-debug

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `--tools-debug` option now enhances readability by pretty-printing JSON tool results, making it easier to inspect and understand the output during debugging.

```CLI
llm chat --tools-debug
```

--------------------------------

### Summarize New York Times Front Page with strip-tags

Source: https://github.com/simonw/llm/blob/main/docs/related-tools.md

Demonstrates how to use `curl`, `strip-tags`, and `llm` to fetch, clean, and summarize HTML content from a URL. `strip-tags` is used to remove HTML tags and filter specific elements, reducing token usage for LLMs.

```bash
curl -s https://www.nytimes.com/ \
  | strip-tags .story-wrapper \
  | llm -s 'summarize the news'
```

--------------------------------

### Find LLM Templates Directory Path

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

Illustrates how to use the `llm templates path` command to display the absolute file system path where `llm` stores its template YAML files.

```bash
llm templates path
```

--------------------------------

### OpenAI Chat Model: o1-2024-12-17 API Reference

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

API documentation for the OpenAI o1-2024-12-17 chat model, detailing its configurable options, supported attachment types, and features, including 'reasoning_effort'.

```APIDOC
OpenAI Chat: o1-2024-12-17
  Options:
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: float
    stop: str
    logit_bias: dict, str
    seed: int
    json_object: boolean
    reasoning_effort: str
  Attachment types:
    application/pdf, image/gif, image/jpeg, image/png, image/webp
  Features:
  - schemas
  - tools
  - async
  Keys:
    key: openai
    env_var: OPENAI_API_KEY
```

--------------------------------

### Save a system prompt as a reusable llm template

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Saves a system prompt as a named template (`pytest`) using the `--save` option. This allows for easy reuse of common system prompts in future `llm` commands, streamlining workflows.

```bash
llm -s 'write pytest tests for this code' --save pytest
```

--------------------------------

### Use standard input as fragment in LLM prompt

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

Illustrates reading fragment content from standard input using `-f -`. This allows piping file content directly into the prompt, making it flexible for various input sources.

```bash
llm -f - 'extract the metadata' < setup.py
```

--------------------------------

### Return Attachments from Tools using `llm.ToolOutput`

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Explains how tools can return rich data, including attachments, by returning an `llm.ToolOutput` instance. This allows tools to provide both a string output and a list of `llm.Attachment` objects, which are then passed to the model for subsequent prompts.

```Python
import llm

def generate_image(prompt: str) -> llm.ToolOutput:
    """Generate an image based on the prompt."""
    image_content = generate_image_from_prompt(prompt)
    return llm.ToolOutput(
        output="Image generated successfully",
        attachments=[llm.Attachment(
            content=image_content,
            mimetype="image/png"
        )],
    )
```

--------------------------------

### Generate Multiple Structured JSON Items with Concise Schema using llm

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Illustrates the use of the '--schema-multi' option with concise schema syntax ('name,bio') to generate multiple structured JSON items. This is useful when the model is expected to produce an array of objects, each conforming to the specified fields.

```bash
llm --schema-multi 'name,bio' 'invent two dogs'
```

--------------------------------

### Viewing Full JSON Definition of a Logged Schema

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

Demonstrates how to retrieve the complete JSON schema definition for a logged schema using its ID. The `--full` flag expands the summary view to show the entire schema structure, including types and descriptions for each property.

```bash
llm schemas --full
```

```json
{
  "type": "object",

```

--------------------------------

### Pass single image attachment to llm using a URL

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Includes an image attachment in a prompt using the `-a` option with a URL. Multi-modal models can then process the image alongside the text prompt.

```bash
llm "describe this image" -a https://static.simonwillison.net/static/2024/pelicans.jpg
```

--------------------------------

### Configuring OpenAI API Key with LLM CLI

Source: https://github.com/simonw/llm/blob/main/docs/openai-models.md

This command configures the LLM tool to use your OpenAI API key. After running it, you will be prompted to paste your API key, which LLM will then store securely for future API calls.

```bash
llm keys set openai
```

--------------------------------

### Using a Custom Embedding Model via CLI with Alias

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/writing-plugins.md

This bash command demonstrates an alternative way to use a custom embedding model from the command line, leveraging a registered alias. It pipes content from `file.txt` to `llm embed`, using the shorter, more convenient alias for the model.

```bash
cat file.txt | llm embed -m all-MiniLM-L6-v2
```

--------------------------------

### Embedding binary content like images

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Explains how to embed binary content, such as images for use with CLIP, by adding the `--binary` option to `llm embed-multi`. This is essential for processing non-textual data types for embedding.

```bash
llm embed-multi photos \
  -m clip \
  --files photos/ '*.jpeg' --binary
```

--------------------------------

### Search LLM Logs with Full-Text Search

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Search `llm` logs using a full-text search index on prompts and responses. The `-q` option returns logs matching the specified search term.

```Shell
llm logs -q SEARCH
```

--------------------------------

### Debug Tool Calls with LLM

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Shows how to use the `--td` (or `--tools-debug`) option to display detailed information about tool execution, including the tool call arguments and return value, useful for debugging tool interactions.

```bash
llm --functions '
def multiply(x: int, y: int) -> int:
    """Multiply two numbers."""
    return x * y
' 'what is 34234 * 213345' --td
```

--------------------------------

### OpenAI Plugin: Processing User Attachments

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

This Python code demonstrates how the OpenAI plugin processes user-provided attachments. It checks for the presence of attachments and constructs the `messages` list for the OpenAI API. The `_attachment` helper function converts various attachment types (images, audio) into the appropriate format for the API, using `base64_content()` for embedding content when a direct URL is not suitable. It covers cases where no text prompt is provided (`prompt.prompt` is `None`).

```python
if not prompt.attachments:
    messages.append({"role": "user", "content": prompt.prompt})
else:
    attachment_message = []
    if prompt.prompt:
        attachment_message.append({"type": "text", "text": prompt.prompt})
    for attachment in prompt.attachments:
        attachment_message.append(_attachment(attachment))
    messages.append({"role": "user", "content": attachment_message})


# And the code for creating the attachment message
def _attachment(attachment):
    url = attachment.url
    base64_content = ""
    if not url or attachment.resolve_type().startswith("audio/"):
        base64_content = attachment.base64_content()
        url = f"data:{attachment.resolve_type()};base64,{base64_content}"
    if attachment.resolve_type().startswith("image/"):
        return {"type": "image_url", "image_url": {"url": url}}
    else:
        format_ = "wav" if attachment.resolve_type() == "audio/wav" else "mp3"
        return {
            "type": "input_audio",
            "input_audio": {
                "data": base64_content,
                "format": format_,
            },
        }
```

--------------------------------

### Browse LLM Completion Logs

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm logs` command provides a way to browse and review previously executed completions. This feature helps users keep track of their interactions and model responses.

```Shell
llm logs
```

--------------------------------

### Access User Data Directory with llm.user_dir()

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-utilities.md

The `llm.user_dir()` function provides the path to LLM's user-specific data directory as a `pathlib.Path` object. This directory is created if it doesn't exist. Plugins can use this function to store their own configuration or logging data in a dedicated subdirectory within the user's LLM data space.

```python
import llm
user_dir = llm.user_dir()
plugin_dir = data_path = user_dir / "my-plugin"
plugin_dir.mkdir(exist_ok=True)
data_path = plugin_dir / "plugin-data.db"
```

--------------------------------

### API Reference: `execute()` Method of LLM Plugin Model

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

This API documentation details the signature and parameters of the `execute()` method, which is central to custom model implementation in `llm` plugins. It describes each argument: `self`, `prompt` (a `Prompt` object), `stream` (a boolean), `response` (a `Response` object), and `conversation` (a `Conversation` object or `None`), explaining their purpose and how they can be used within the model's execution logic.

```APIDOC
def execute(self, prompt, stream, response, conversation):
  Parameters:
    prompt (Prompt): An object containing the user's text, system prompt, and provided options.
    stream (bool): Indicates if the model is being run in streaming mode.
    response (Response): The Response object being created, allowing additional information to be written to response.response_json for logging.
    conversation (Conversation | None): The Conversation object the prompt is part of, or None. Can be used to access previous prompts and responses for context.
  Returns:
    (Generator): A generator yielding parts of the model's response.
```

--------------------------------

### Continue Previous Conversation using llm

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Shows how to use the '-c' or '--continue' option to continue the most recent conversation. This re-sends previous prompts and responses, allowing for a natural flow of dialogue with the language model, though it can increase token usage and cost.

```bash
llm 'More names' -c
```

--------------------------------

### View Details for Specific LLM Models by ID

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm models` command now accepts the `-m` option multiple times, allowing users to specify several model IDs to retrieve detailed information for only those particular models.

```Bash
llm models -m gpt-4 -m gpt-3.5-turbo
```

--------------------------------

### Pipe an attachment to llm via standard input

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Pipes an attachment (e.g., an image) to `llm` using standard input by specifying `-` as the filename for `-a`. `llm` attempts to automatically detect the content type.

```bash
cat image.jpg | llm "describe this image" -a -
```

--------------------------------

### Configure OpenAI-Compatible Model via YAML

Source: https://github.com/simonw/llm/blob/main/docs/other-models.md

This YAML configuration snippet shows how to add an OpenAI-compatible model, like `orca-mini-3b` hosted by LocalAI, to LLM's `extra-openai-models.yaml` file. It specifies a unique `model_id`, the actual `model_name` for the API, and the `api_base` URL for the compatible API endpoint.

```yaml
- model_id: orca-openai-compat
  model_name: orca-mini-3b.ggmlv3
  api_base: "http://localhost:8080"
```

--------------------------------

### Fragment Loader Returning Multiple Fragments and Attachments

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-hooks.md

This Python function illustrates an advanced use case for fragment loaders, where the `my_fragment_loader` returns a list containing a mix of `llm.Fragment` objects and `llm.Attachment` objects. This is particularly useful for scenarios like processing multiple files from a directory, ensuring individual caching and efficient handling.

```python
def my_fragment_loader(argument: str) -> list[llm.Fragment]:
    "Docs go here."
    return [
        llm.Fragment("Fragment 1 content", "my-fragments:{argument}"),
        llm.Fragment("Fragment 2 content", "my-fragments:{argument}"),
        llm.Attachment(path="/path/to/image.png")
    ]
```

--------------------------------

### Utilize Perplexity Labs API Models with llm-perplexity

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-perplexity plugin, developed by Alexandru Geana, supports Perplexity Labs API models, including `llama-3-sonar-large-32k-online` for online search and `llama-3-70b-instruct`.

```APIDOC
Plugin: llm-perplexity
  API Provider: Perplexity Labs
  Models Supported: llama-3-sonar-large-32k-online (online search), llama-3-70b-instruct
  Purpose: Accesses Perplexity Labs API models.
```

--------------------------------

### llm.Template Class API Reference

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-hooks.md

Reference for the `llm.Template` class, used to define prompt templates for the LLM library. It encapsulates the template's name, main prompt content, and system instructions for the language model.

```APIDOC
llm.Template:
  __init__(name: str, prompt: str, system: str)
    name: The unique name of the template.
    prompt: The main prompt content for the template.
    system: The system instructions for the template.
```

--------------------------------

### Embedding data from files in directories

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Demonstrates how to embed content from multiple text files within a specified directory structure using `llm embed-multi` with `--files` and glob patterns. This command efficiently processes all matching files and stores their embeddings.

```bash
llm embed-multi documentation \
  -m 3-small \
  --files docs '**/*.md' \
  -d documentation.db \
  --store
```

--------------------------------

### Insert Fragments into llm chat Sessions

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Users can now insert content fragments into `llm chat` sessions using the `!fragment <id>` command. Initial fragments can also be pre-loaded into a chat session using the `-f` or `--sf` command-line options.

```CLI
!fragment <id>
llm chat -f <fragment_id>
llm chat --sf <fragment_id>
```

--------------------------------

### Define and Call a Custom Python Function with LLM

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Demonstrates how to define an inline Python function using the `--functions` option directly in the command line and have the LLM call it to perform a calculation.

```bash
llm --functions '
def multiply(x: int, y: int) -> int:
    """Multiply two numbers."""
    return x * y
' 'what is 34234 * 213345'
```

--------------------------------

### Register Synchronous and Asynchronous LLM Models with Plugin Hook

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

This snippet demonstrates how to use the `register_models` plugin hook to register both synchronous and asynchronous model instances. It also shows how to assign aliases to models, allowing them to be invoked using alternative names.

```Python
@hookimpl
def register_models(register):
    register(
        MyModel(), MyAsyncModel(), aliases=("my-model-aliases",)
    )
```

--------------------------------

### Show a Stored LLM Schema

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Displays the content of a specific stored schema identified by its ID. This allows for detailed examination of a schema's structure.

```Shell
Usage: llm schemas show [OPTIONS] SCHEMA_ID

  Show a stored schema

Options:
  -d, --database FILE  Path to log database
  -h, --help           Show this message and exit.
```

--------------------------------

### Enabling JSON Output for OpenAI Models in LLM

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Shows how to configure OpenAI models in LLM to return output as a valid JSON object using the `-o json_object 1` option, useful for structured data generation.

```Shell
llm -m gpt-4-turbo -o json_object 1 '{"prompt": "Generate a JSON object with a \"name\" and \"age\" field."}'
```

--------------------------------

### LLM YAML Template with Default Options

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

Shows how to set default model `options` like `temperature` within a YAML template. These settings are automatically applied when the template is used, ensuring consistent model behavior.

```yaml
name: wild-french
system: Speak in French
options:
  temperature: 1.8
```

--------------------------------

### Using a Custom Embedding Model via CLI with Full ID

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/writing-plugins.md

This bash command illustrates how to use a custom embedding model, registered through a plugin, directly from the command line. It pipes content from `file.txt` to the `llm embed` command, specifying the model using its full `model_id`.

```bash
cat file.txt | llm embed -m sentence-transformers/all-MiniLM-L6-v2
```

--------------------------------

### Retrieve API Keys and Secrets with llm.get_key()

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-utilities.md

The `llm.get_key()` method allows plugins to securely retrieve API keys or other secrets stored by users. It supports looking up keys by alias, falling back to environment variables, and resolving keys from user-provided input. This function returns the key as a string or `None` if not found.

```python
github_key = llm.get_key(alias="github")
```

```python
github_key = llm.get_key(alias="github", env="GITHUB_TOKEN")
```

```python
github_key = llm.get_key(input=input_from_user, alias="github", env="GITHUB_TOKEN")
```

--------------------------------

### Migrate LLM Logs Database to New Location

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This sequence of commands migrates an existing `logs.db` database from its old location (`~/.llm/log.db`) to the new, OS-specific path. After copying, the old directory is removed to tidy up the system.

```bash
cp ~/.llm/log.db "$(llm logs path)"
rm -rf ~/.llm # To tidy up the now obsolete directory
```

--------------------------------

### Extending LLM Logs with Custom Plugin Data

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

This Python code demonstrates how a custom LLM plugin can enrich the automatically generated log entries. By assigning a dictionary to `response.response_json` within the `execute()` method, plugins can store additional, custom information (like a 'transitions' table) directly within the log database.

```python
    def execute(self, prompt, stream, response, conversation):
        text = self.prompt.prompt
        transitions = build_markov_table(text)
        for word in generate(transitions, 20):
            yield word + ' '
        response.response_json = {"transitions": transitions}
```

--------------------------------

### CLI: Prepending Text for Multi-Embeddings

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm embed-multi` command introduces a `--prepend X` option to add a specified string to the beginning of each value before embedding, useful for models requiring specific prefixes like 'search_document: '.

```Shell
llm embed-multi --prepend "search_document: " "Your text to embed" "Another document"
```

--------------------------------

### List specific LLM models by ID or alias using `llm models -m`

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Specify one or more `-m` options with a model ID or alias to display information only for those particular models.

```bash
llm models -m gpt-4o -m gemini-1.5-pro-002
```

--------------------------------

### Enter Multi-line Input in LLM Chat

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Illustrates how to use the `!multi` command within an interactive `llm chat` session to input multiple lines of text, useful for pasting code or error messages. It also shows how to define a custom end delimiter to avoid conflicts with `!end` within the pasted text.

```console
Chatting with gpt-4
Type 'exit' or 'quit' to exit
Type '!multi' to enter multiple lines, then '!end' to finish
Type '!edit' to open your default editor and modify the prompt.
Type '!fragment <my_fragment> [<another_fragment> ...]' to insert one or more fragments
> !multi custom-end
 Explain this error:

   File "/opt/homebrew/Caskroom/miniconda/base/lib/python3.10/urllib/request.py", line 1391, in https_open
    return self.do_open(http.client.HTTPSConnection, req,
  File "/opt/homebrew/Caskroom/miniconda/base/lib/python3.10/urllib/request.py", line 1351, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>

 !end custom-end
```

--------------------------------

### CLI: Display Token Usage for Prompts and Logs

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

These CLI commands allow users to view token usage information. The `--usage` flag can be appended to `llm prompt` to display token usage after a response, and to `llm logs` to show usage details for previously logged responses.

```CLI
llm prompt ... -u/--usage
```

```CLI
llm logs -u/--usage
```

--------------------------------

### Browse previously stored LLM fragments

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

Explains how to view a truncated list of fragments previously stored in the LLM database using the `llm fragments` command. The output includes hash IDs, aliases, and source information.

```bash
llm fragments
```

--------------------------------

### Calculate and Summarize Embedding Clusters with llm-cluster

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-cluster plugin adds a `llm cluster` command for calculating clusters from a collection of embeddings. The identified clusters can then be passed to a Large Language Model to generate descriptive summaries, aiding in the analysis and understanding of embedding spaces.

```Shell
llm cluster [options]
```

--------------------------------

### Execute Python Functions as Tools with LLM

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Demonstrates how to enable LLM models to execute Python functions as tools. This functionality is available via both the command-line interface and the Python API, allowing models to perform computations by calling defined Python functions.

```bash
llm --functions '
def multiply(x: int, y: int) -> int:
    """Multiply two numbers."""
    return x * y
' 'what is 34234 * 213345'
```

```python
import llm

def multiply(x: int, y: int) -> int:
    """Multiply two numbers."""
    return x * y

model = llm.get_model("gpt-4.1-mini")
response = model.chain(
    "What is 34234 * 213345?",
    tools=[multiply]
)
print(response.text())
```

--------------------------------

### Integrate Meta Llama 2 and 3 via Amazon Bedrock with llm-bedrock-meta

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-bedrock-meta plugin, by Fabian Labat, adds support for Llama 2 and Llama 3 by Meta via Amazon Bedrock. It enables LLM to utilize Meta's Llama models through AWS Bedrock.

```APIDOC
Plugin: llm-bedrock-meta
  API Provider: Amazon Bedrock (for Meta models)
  Models Supported: Llama 2, Llama 3 by Meta
  Purpose: Provides support for Meta's Llama models via Amazon Bedrock.
```

--------------------------------

### Jinja2 Base Template for Dynamic Page Titles

Source: https://github.com/simonw/llm/blob/main/docs/_templates/base.html

This Jinja2 snippet establishes the base HTML structure by extending `!base.html` and implements logic within the `htmltitle` block to dynamically set the page's title. It checks if `docstitle` is present, if the current page is the `master_doc`, or falls back to a default title, ensuring proper display across different documentation pages. It also includes a `site_meta` block.

```Jinja2
{%- extends "!base.html" %} {%- block htmltitle -%} {% if not docstitle %} {{ title|striptags|e }} {% elif pagename == master_doc %} LLM: A CLI utility and Python library for interacting with Large Language Models {% else %} {{ title|striptags|e }} - {{ docstitle|striptags|e }} {% endif %} {%- endblock -%} {% block site_meta %} {{ super() }} {% endblock %}
```

--------------------------------

### Guess Tool Functionality from Python Tests with Symbex and LLM

Source: https://github.com/simonw/llm/blob/main/docs/related-tools.md

Demonstrates using `symbex` to extract Python test functions matching a pattern (`test*csv*`) and piping them to `llm` to infer the software's purpose based on its tests.

```bash
symbex 'test*csv*' | \
  llm --system 'based on these tests guess what this tool does'
```

--------------------------------

### Search LLM Logs by Term

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

This command allows you to search the `prompt` or `response` columns of your logs for a specific search term. The most relevant results will be displayed at the end of the output.

```bash
llm logs -q 'cheesecake'
```

--------------------------------

### Execute llm prompt without streaming output

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Runs a prompt using `llm`, but waits for the complete response before displaying it. The `--no-stream` flag disables the default token streaming behavior.

```bash
llm 'Ten names for cheesecakes' --no-stream
```

--------------------------------

### llm embed-multi Command Overview and Options

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

The `llm embed-multi` command allows embedding multiple strings efficiently, leveraging model batching capabilities. It supports various input sources (CSV, TSV, JSON files, SQLite queries, directories with glob patterns) and offers options for model selection, database specification, content storage, ID prefixing, content prepending, and batch sizing.

```APIDOC
llm embed-multi:
  description: Embed multiple strings at once, leveraging model batching.
  input_sources:
    - CSV, TSV, JSON, newline-delimited JSON file
    - SQLite database with SQL query
    - Directories with glob patterns
  options:
    - -m model_id (string): Specify the embedding model to use.
    - -d database.db (string): Specify a different database file.
    - --store (boolean): Store original content in the embeddings table.
    - --prefix (string): Prepend a prefix to the stored ID.
    - --prepend (string): Prepend a string to content before embedding (e.g., 'search_document: ').
    - --batch-size SIZE (integer): Process embeddings in batches.
```

--------------------------------

### Verifying Custom Plugin Data in LLM Logs

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

After a plugin has been configured to add custom data to the `response_json`, this snippet shows how to re-run the `llm logs` command to verify that the additional information, such as the 'transitions' table, is successfully included in the logged response. The JSON output confirms the presence of the custom data.

```bash
llm logs -n 1
```

```json
[
  {
    "id": 623,
    "model": "markov",
    "prompt": "the cat sat on the mat",
    "system": null,
    "prompt_json": null,
    "options_json": {},
    "response": "on the mat the cat sat on the cat sat on the mat sat on the cat sat on the ",
    "response_json": {
      "transitions": {
        "the": [
          "cat",
          "mat"
        ],
        "cat": [
          "sat"
        ],
        "sat": [
          "on"
        ],
        "on": [
          "the"
        ]
      }
    },
    "reply_to_id": null,
    "chat_id": null,
    "duration_ms": 0,
    "datetime_utc": "2023-07-06T01:34:45.376637"
  }
]
```

--------------------------------

### Querying LLM Logs for Response Details and Log Probabilities

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Demonstrates how to access and parse the `llm` SQLite logs database to retrieve and inspect recorded model responses, including log probabilities. This uses `sqlite-utils` and `jq` for data extraction and formatting.

```bash
sqlite-utils "$(llm logs path)" \
  'select * from responses order by id desc limit 1' | \
  jq '.[0].response_json' -r | jq
```

```JSON
[
    {
      "text": "Hi",
      "top_logprobs": [
        {
          "Hi": -0.13706253,
          "Hello": -2.3714375,
          "Hey": -3.3714373
        }
      ]
    },
    {
      "text": " there",
      "top_logprobs": [
        {
          " there": -0.96057636,
          "!\"": -0.5855763,
          ".\"": -3.2574513
        }
      ]
    }
  ]
```

--------------------------------

### Edit Prompt in LLM Chat Editor

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Demonstrates how to use the `!edit` command during an `llm chat` session to open the default text editor. This allows users to compose or modify their prompt in a full editor before sending it to the model.

```console
Chatting with gpt-4
Type 'exit' or 'quit' to exit
Type '!multi' to enter multiple lines, then '!end' to finish
Type '!edit' to open your default editor and modify the prompt.
Type '!fragment <my_fragment> [<another_fragment> ...]' to insert one or more fragments
> !edit
```

--------------------------------

### Output llm schemas list in JSON Format

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm schemas list` command now supports outputting schema definitions in JSON format for programmatic access. Use `--json` for standard JSON or `--nl` for newline-delimited JSON.

```CLI
llm schemas list --json
llm schemas list --nl
```

--------------------------------

### Model Updates and Aliases

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

New models like `chatgpt-4o-latest`, `o3-mini`, `o1`, `gpt-4o-audio-preview`, `gpt-4o-mini-audio-preview` have been added. `o3-mini` and `o1` now support `reasoning_effort` (`low`, `medium`, `high`). OpenAI embedding models now use full names (`text-embedding-ada-002`, etc.) with aliases for previous names.

```APIDOC
New Models:
  chatgpt-4o-latest
  o3-mini
  o1
  gpt-4o-audio-preview
  gpt-4o-mini-audio-preview

Model Options:
  o3-mini, o1:
    reasoning_effort: str (low, medium, high)

OpenAI Embedding Models:
  Full Names:
    text-embedding-ada-002
    text-embedding-3-small
    text-embedding-3-large
  Aliases: (Previous names still supported)
```

--------------------------------

### Define and Execute Tools with LLM Python API

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Explains how to define Python functions as tools for the LLM model, retrieve tool calls from the response, and execute them. It also covers using `model.chain()` for automatic tool execution and streaming responses from a chain of operations.

```python
import llm

def upper(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()

model = llm.get_model("gpt-4.1-mini")
response = model.prompt("Convert panda to upper", tools=[upper])
tool_calls = response.tool_calls()
# [ToolCall(name='upper', arguments={'text': 'panda'}, tool_call_id='...')]
```

```python
tool_results = response.execute_tool_calls()
# [ToolResult(name='upper', output='PANDA', tool_call_id='...')]
```

```python
chain_response = model.chain(
    "Convert panda to upper",
    tools=[upper],
)
print(chain_response.text())
# The word "panda" converted to uppercase is "PANDA".
```

```python
for chunk in model.chain(
    "Convert panda to upper",
    tools=[upper],
):
    print(chunk, end="", flush=True)
```

```python
chain = model.chain(
    "Convert panda to upper",
    tools=[upper],
)
for response in chain.responses():
    print(response.prompt)
    for chunk in response:
        print(chunk, end="", flush=True)
```

--------------------------------

### Saving LLM Schemas as Reusable Templates

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

To promote reusability, LLM allows users to save schema definitions as named templates. This is achieved using the `llm --save` option, which associates a concise DSL schema with a user-defined name. Once saved, these templates can be easily referenced and applied in subsequent LLM commands without retyping the full schema definition.

```bash
llm --schema 'name, age int, one_sentence_bio' --save dog
```

--------------------------------

### Embed Binary Data from File using llm embed

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Shows how to process binary data, such as an image file, using `llm embed` with the `--binary` and `-i` options. This is useful for models like `llm-clip` that can handle non-textual inputs.

```bash
llm embed --binary -m clip -i image.jpg
```

--------------------------------

### LLM Python API: model.chain() Method

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Documentation for the `model.chain()` method in the LLM Python API, used for executing multiple prompts in a sequence, especially when integrating with tool execution. It facilitates complex interactions where models might need to call external functions.

```APIDOC
model.chain(prompt: str, tools: list = None) -> Response
  Description: Executes multiple prompts in a sequence, enabling tool integration.
  Parameters:
    prompt (str): The initial prompt string for the model.
    tools (list, optional): A list of Python functions to be made available as tools to the model. Defaults to None.
  Returns:
    Response: An object containing the model's output, which can be accessed via methods like .text().
```

--------------------------------

### Embedding data from SQLite (same database)

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Explains how to embed data from a SQLite database into the same database using `llm embed-multi` with `--sql`. This is useful when your source data and embeddings reside in the same `docs.db` file.

```bash
llm embed-multi docs \
  -d docs.db \
  --sql 'select id, title, content from documents' \
  -m 3-small
```

--------------------------------

### Add Support for Replicate Hosted Models via llm-replicate

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-replicate plugin adds support for remote models hosted on Replicate, including Llama 2 from Meta AI. It expands LLM's capabilities to models available on the Replicate platform.

```APIDOC
Plugin: llm-replicate
  API Provider: Replicate
  Models Supported: Remote models hosted on Replicate (e.g., Llama 2 from Meta AI)
  Purpose: Provides access to models hosted on Replicate.
```

--------------------------------

### llm Default Model Configuration API Methods

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Documentation for new API methods in the `llm` library for managing default LLM and embedding models. These methods allow programmatic control over which models are used by default.

```APIDOC
llm.get_default_model() -> Model
llm.set_default_model(alias: str) -> None
llm.get_default_embedding_model(alias: str) -> EmbeddingModel
llm.set_default_embedding_model() -> None
```

--------------------------------

### Store Content and Metadata with llm embed

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

This command demonstrates how to use the `llm embed` CLI tool to generate embeddings for a single string while simultaneously storing the original content and arbitrary JSON metadata in the database. The `--store` option saves the text, and `--metadata` saves the JSON object.

```bash
llm embed phrases hound -c 'my happy hound' --store
```

```bash
llm embed phrases hound \
  -m 3-small \
  -c 'my happy hound' \
  --metadata '{"name": "Hound"}' \
  --store
```

--------------------------------

### Generate Multiple Items with LLM's DSL

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Learn to use `llm.schema_dsl()` with the `multi=True` parameter to instruct the LLM to generate a list of items, each conforming to the specified schema. Useful for generating multiple structured entities.

```python
print(model.prompt(
    "Describe 3 nice dogs with surprising names",
    schema=llm.schema_dsl("name, age int, bio", multi=True)
))
```

--------------------------------

### Convert PDFs to Markdown Fragments with llm-fragments-pdf

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-fragments-pdf plugin converts PDF documents into Markdown format using PyMuPDF4LLM, making their content accessible as fragments for LLM. This allows users to ask questions or summarize information contained within PDF files. The command specifies the path to the PDF file.

```Shell
llm -f pdf:something.pdf "what's this about?"
```

--------------------------------

### Truncate Text to Desired Token Count with ttok

Source: https://github.com/simonw/llm/blob/main/docs/related-tools.md

Illustrates using `ttok` to truncate input text to a specified number of OpenAI tokens, useful for fitting large documents into LLM context windows.

```bash
ttok This is too many tokens -t 3
```

--------------------------------

### Combine multi-line input and fragments in LLM chat

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

Illustrates using the `!multi` command to enter multi-line prompts and combine them with `!fragment` commands. This allows including multiple fragments within a single, complex chat turn.

```bash
!multi
Explain the difference between fragments and templates to me
!fragment https://llm.datasette.io/en/stable/fragments.html https://llm.datasette.io/en/stable/templates.html
!end
```

--------------------------------

### Python API: Retrieve Available Models

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

These Python functions provide programmatic access to list available models. `llm.get_models()` returns synchronous models, while `llm.get_async_models()` retrieves asynchronous models, enabling dynamic model selection within applications.

```APIDOC
llm.get_models() -> List[Model]
llm.get_async_models() -> List[AsyncModel]
```

--------------------------------

### Ensuring LLM Plugin User Directory Existence

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Documents the `llm.user_dir()` function, primarily used by plugins, which ensures that the necessary user directory exists before returning its path. This prevents file system errors during plugin operations.

```Python
llm.user_dir()
```

--------------------------------

### Finding LLM Configuration Directory

Source: https://github.com/simonw/llm/blob/main/docs/openai-models.md

This command helps locate the directory where LLM stores its logs and configuration files, such as `extra-openai-models.yaml`. Knowing this path is essential for manually adding or modifying model configurations.

```bash
dirname "$(llm logs path)"
```

--------------------------------

### Python API: Register Response Completion Callback

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

These methods enable the registration of a callback function to be executed once a response has fully completed. `response.on_done()` is for synchronous operations, and `await response.on_done()` for asynchronous, providing a mechanism for post-response processing.

```APIDOC
response.on_done(callback: Callable)
await response.on_done(callback: Callable)
```

--------------------------------

### Importing Optional Type for Model Options

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Shows the necessary import statement for `Optional` from the `typing` module, which is used to define optional fields in the model's `Options` class.

```python
from typing import Optional
```

--------------------------------

### Searching for similar embeddings from a file

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Explains how to provide input text for similarity search from a file using the `-i filename` option with `llm similar`. This is useful for comparing against longer texts or pre-existing content.

```bash
llm similar quotations -i one.txt
```

--------------------------------

### Importing Pydantic Validation Tools

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

Specifies the required imports from the Pydantic library, `field_validator` and `Field`, which are essential for adding advanced validation rules and inline documentation to model options.

```python
from pydantic import field_validator, Field
```

--------------------------------

### Viewing Recent LLM Log Entries

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

This snippet shows how to use the `llm logs` command to retrieve and display the single most recent entry from the LLM's internal SQLite database, which automatically logs prompts and responses. The accompanying JSON illustrates the default structure of a logged entry.

```bash
llm logs -n 1
```

```json
[
  {
    "id": "01h52s4yez2bd1qk2deq49wk8h",
    "model": "markov",
    "prompt": "the cat sat on the mat",
    "system": null,
    "prompt_json": null,
    "options_json": {},
    "response": "on the cat sat on the cat sat on the mat cat sat on the cat sat on the cat ",
    "response_json": null,
    "conversation_id": "01h52s4yey7zc5rjmczy3ft75g",
    "duration_ms": 0,
    "datetime_utc": "2023-07-11T15:29:34.685868",
    "conversation_name": "the cat sat on the mat",
    "conversation_model": "markov"
  }
]
```

--------------------------------

### Integrate Cohere Command R and Plus Models via llm-command-r

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-command-r plugin supports Cohere's Command R and Command R Plus API models. This allows LLM to utilize Cohere's advanced generative models for various tasks.

```APIDOC
Plugin: llm-command-r
  API Provider: Cohere
  Models Supported: Command R, Command R Plus
  Purpose: Provides access to Cohere's Command R API models.
```

--------------------------------

### Enable Tools Debugging via Environment Variable

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

A new environment variable, `LLM_TOOLS_DEBUG`, has been introduced to permanently enable the `--tools-debug` functionality, allowing for consistent debugging across sessions without needing to specify the flag every time.

```Shell
export LLM_TOOLS_DEBUG=1
```

--------------------------------

### Using Attachments with llm CLI and Python API

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This snippet demonstrates how to include image attachments when prompting LLM models, both through the command-line interface and the Python API. Attachments can be provided as URLs, local file paths, or binary data, supporting multi-modal model interactions.

```bash
llm -m gpt-4o "describe this image" \
  -a https://static.simonwillison.net/static/2024/pelicans.jpg
```

```bash
llm -m gpt-4o-mini "extract text" -a image1.jpg -a image2.jpg
```

```bash
cat image | llm -m gpt-4o-mini "extract text" --attachment-type - image/jpeg
```

```python
model = llm.get_model("gpt-4o-mini")
response = model.prompt(
    "Describe these images",
    attachments=[
        llm.Attachment(path="pelican.jpg"),
        llm.Attachment(url="https://static.simonwillison.net/static/2024/pelicans.jpg")
    ]
)
```

--------------------------------

### Query Specific Columns from SQLite Table

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

Use `sqlite-utils rows` to display selected columns (name, organization, role) from the `people` table in `data.db` in a tabular format.

```bash
sqlite-utils rows data.db people -t -c name -c organization -c role
```

--------------------------------

### Configure OpenAI-Compatible Model with Custom HTTP Headers

Source: https://github.com/simonw/llm/blob/main/docs/other-models.md

This YAML configuration demonstrates how to add an OpenAI-compatible model that requires additional HTTP headers, such as those for `openrouter.ai`. It includes `model_id`, `model_name`, `api_base`, `api_key_name`, and a `headers` block for custom HTTP headers like `HTTP-Referer` and `X-Title`.

```yaml
- model_id: claude
  model_name: anthropic/claude-2
  api_base: "https://openrouter.ai/api/v1"
  api_key_name: openrouter
  headers:
    HTTP-Referer: "https://llm.datasette.io/"
    X-Title: LLM
```

--------------------------------

### Process URLs with Jina Reader API as Fragments with llm-fragments-reader

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-fragments-reader plugin processes a given URL through the Jina Reader API, which extracts clean, readable content from web pages. This extracted content is then used as a fragment for LLM, allowing for focused summarization or analysis of web articles. The command specifies the URL to process.

```Shell
llm -f 'reader:https://simonwillison.net/tags/jina/' summary
```

--------------------------------

### Output Embeddings in Different Formats with llm embed

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Demonstrates how to output embeddings in various formats such as raw bytes (`blob`), hexadecimal (`hex`), or Base64 using the `--format` option. This is useful for integrating with different storage or transmission needs.

```bash
llm embed -c 'This is some content' -m 3-small --format base64
```

--------------------------------

### llm uninstall --help

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Uninstalls specified Python packages from the LLM environment. It includes an option to bypass the confirmation prompt during uninstallation.

```APIDOC
Usage: llm uninstall [OPTIONS] PACKAGES...

  Uninstall Python packages from the LLM environment

Options:
  -y, --yes   Don't ask for confirmation
  -h, --help  Show this message and exit.
```

--------------------------------

### Check for Binary Input Support and Embed Binary Data

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/python-api.md

Illustrates how to check if an embedding model supports binary input using `supports_binary` and then embed a byte string, such as an image file.

```Python
if embedding_model.supports_binary:
    vector = embedding_model.embed(open("my-image.jpg", "rb").read())
```

--------------------------------

### List All Embedding Collections with llm CLI

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

This command displays all collections stored in the embeddings database. It provides an overview of available data collections that have been created or imported.

```bash
llm collections list
```

--------------------------------

### SQL Schema for logs.db Database

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

This SQL schema defines the structure of the `logs.db` database, which stores data related to LLM interactions. It includes tables for conversations, responses, attachments, fragments, and tools, along with their respective columns and foreign key relationships. The `responses_fts` table is configured for SQLite full-text search on prompt and response content.

```SQL
CREATE TABLE [conversations] (
  [id] TEXT PRIMARY KEY,
  [name] TEXT,
  [model] TEXT
);
CREATE TABLE [schemas] (
  [id] TEXT PRIMARY KEY,
  [content] TEXT
);
CREATE TABLE "responses" (
  [id] TEXT PRIMARY KEY,
  [model] TEXT,
  [prompt] TEXT,
  [system] TEXT,
  [prompt_json] TEXT,
  [options_json] TEXT,
  [response] TEXT,
  [response_json] TEXT,
  [conversation_id] TEXT REFERENCES [conversations]([id]),
  [duration_ms] INTEGER,
  [datetime_utc] TEXT,
  [input_tokens] INTEGER,
  [output_tokens] INTEGER,
  [token_details] TEXT,
  [schema_id] TEXT REFERENCES [schemas]([id]),
  [resolved_model] TEXT
);
CREATE VIRTUAL TABLE [responses_fts] USING FTS5 (
  [prompt],
  [response],
  content=[responses]
);
CREATE TABLE [attachments] (
  [id] TEXT PRIMARY KEY,
  [type] TEXT,
  [path] TEXT,
  [url] TEXT,
  [content] BLOB
);
CREATE TABLE [prompt_attachments] (
  [response_id] TEXT REFERENCES [responses]([id]),
  [attachment_id] TEXT REFERENCES [attachments]([id]),
  [order] INTEGER,
  PRIMARY KEY ([response_id],
  [attachment_id])
);
CREATE TABLE [fragments] (
  [id] INTEGER PRIMARY KEY,
  [hash] TEXT,
  [content] TEXT,
  [datetime_utc] TEXT,
  [source] TEXT
);
CREATE TABLE [fragment_aliases] (
  [alias] TEXT PRIMARY KEY,
  [fragment_id] INTEGER REFERENCES [fragments]([id])
);
CREATE TABLE "prompt_fragments" (
  [response_id] TEXT REFERENCES [responses]([id]),
  [fragment_id] INTEGER REFERENCES [fragments]([id]),
  [order] INTEGER,
  PRIMARY KEY ([response_id],
  [fragment_id],
  [order])
);
CREATE TABLE "system_fragments" (
  [response_id] TEXT REFERENCES [responses]([id]),
  [fragment_id] INTEGER REFERENCES [fragments]([id]),
  [order] INTEGER,
  PRIMARY KEY ([response_id],
  [fragment_id],
  [order])
);
CREATE TABLE [tools] (
  [id] INTEGER PRIMARY KEY,
  [hash] TEXT,
  [name] TEXT,
  [description] TEXT,
  [input_schema] TEXT,
  [plugin] TEXT
);
CREATE TABLE [tool_responses] (
  [tool_id] INTEGER REFERENCES [tools]([id]),
  [response_id] TEXT REFERENCES [responses]([id]),
  PRIMARY KEY ([tool_id],
  [response_id])
);
CREATE TABLE [tool_calls] (
  [id] INTEGER PRIMARY KEY,
  [response_id] TEXT REFERENCES [responses]([id]),
  [tool_id] INTEGER REFERENCES [tools]([id]),
  [name] TEXT,
  [arguments] TEXT,
  [tool_call_id] TEXT
);
CREATE TABLE "tool_results" (
  [id] INTEGER PRIMARY KEY,
  [response_id] TEXT REFERENCES [responses]([id]),
  [tool_id] INTEGER REFERENCES [tools]([id]),
  [name] TEXT,
  [output] TEXT,
  [tool_call_id] TEXT,
  [instance_id] INTEGER REFERENCES [tool_instances]([id]),
  [exception] TEXT
);
CREATE TABLE [tool_instances] (
  [id] INTEGER PRIMARY KEY,
  [plugin] TEXT,
  [name] TEXT,
  [arguments] TEXT
);
```

--------------------------------

### Convert Websites to Markdown Fragments with llm-fragments-site-text

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-fragments-site-text plugin converts the main text content of a website into Markdown using Trafilatura, enabling its use as fragments for LLM. This is useful for summarizing web pages or extracting information from online articles. The command specifies the URL of the website.

```Shell
llm -f site:https://example.com "summarize this"
```

--------------------------------

### Integrate Grok Model using xAI API with llm-grok

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-grok plugin, by Benedikt Hiepler, provides access to the Grok model using the xAI API. It enables LLM to interact with xAI's Grok model.

```APIDOC
Plugin: llm-grok
  API Provider: xAI
  Models Supported: Grok model
  Purpose: Provides access to the Grok model via xAI API.
```

--------------------------------

### List Available Embedding Models with `llm embed-models list`

Source: https://github.com/simonw/llm/blob/main/docs/help.md

The `llm embed-models list` subcommand displays all currently available embedding models. It includes an option to filter the list by providing a query string to search for specific models.

```Shell
Usage: llm embed-models list [OPTIONS]

  List available embedding models

Options:
  -q, --query TEXT  Search for embedding models matching these strings
  -h, --help        Show this message and exit.
```

--------------------------------

### Define LLM Template with a Variable Parameter

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This YAML snippet shows how to define a prompt template that includes a variable, `$voice`. This allows the template to be more flexible, accepting dynamic input for specific parts of the prompt, such as the desired tone or style.

```yaml
system: Summarize this text in the voice of $voice
```

--------------------------------

### Utilize a Custom Toolbox Instance in `llm.conversation`

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Shows how to instantiate and use a custom `llm.Toolbox` class, such as the `Memory` toolbox, within an `llm.conversation`. This enables the model to interact with the stateful tools, demonstrating how the shared memory persists across different prompts in a conversation.

```Python
model = llm.get_model("gpt-4.1-mini")
memory = Memory()

conversation = model.conversation(tools=[memory])
print(conversation.chain("Set name to Simon", after_call=print).text())

print(memory._memory)
# Should show {'name': 'Simon'}

print(conversation.chain("Set name to Penguin", after_call=print).text())
# Now it should be {'name': 'Penguin'}

print(conversation.chain("Print current name", after_call=print).text())
```

--------------------------------

### Listing All LLM Model Aliases (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/aliases.md

This command lists all currently configured model aliases in the LLM tool, showing the short alias name and its corresponding full model ID. It provides a quick overview of available shortcuts for models.

```bash
llm aliases
```

--------------------------------

### Generate Code with LLM System Prompt

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm` tool can be used with a `--code` option to set a system prompt specifically designed to encourage the output of programming code. This ensures the model generates code without additional explanatory text, useful for direct code generation tasks.

```Shell
llm "Python code to output factorial 10" --code
```

--------------------------------

### Handle Multi-modal Attachments with LLM Python API

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Illustrates how to pass multi-modal inputs like images (from file paths, URLs, or binary content) to models that support attachments. It also demonstrates how to check which attachment types a specific model supports.

```python
import llm

model = llm.get_model("gpt-4o-mini")
response = model.prompt(
    "Describe these images",
    attachments=[
        llm.Attachment(path="pelican.jpg"),
        llm.Attachment(url="https://static.simonwillison.net/static/2024/pelicans.jpg")
    ]
)
```

```python
model = llm.get_model("gpt-4o-mini")
print(model.attachment_types)
# {'image/gif', 'image/png', 'image/jpeg', 'image/webp'}

if "image/jpeg" in model.attachment_types:
    # Use a JPEG attachment here
    ...
```

--------------------------------

### Inspect and Manage Embeddings Database

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Covers the `llm embed-db` command, providing functionalities for inspecting and working with the default embeddings SQLite database.

```CLI
llm embed-db <subcommand>
```

--------------------------------

### Register Custom Fragment Loaders in LLM Plugins

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm` tool introduces a new `register_fragment_loaders()` plugin hook. This allows developers to extend LLM's functionality by registering custom methods for loading fragments, enhancing data processing capabilities.

```Python
from llm.plugins import register_fragment_loaders

@register_fragment_loaders
def my_fragment_loader(text: str):
    # Custom logic to load fragments from text
    return ["fragment1", "fragment2"]
```

--------------------------------

### Retrieving a List of All Available LLM Models

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Explains how to use `llm.get_models()` to retrieve a list of all available language models, including those provided by plugins. This is useful for discovering and selecting models programmatically for various tasks.

```python
import llm

for model in llm.get_models():
    print(model.model_id)
```

--------------------------------

### Retrieve LLM Logs Database Path

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This command displays the current file system path where the LLM tool stores its `logs.db` database. This path is operating system-dependent and helps users locate the database for inspection or backup.

```bash
llm logs path
```

--------------------------------

### Registering Custom LLM Prompt Template Loaders

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-hooks.md

This snippet demonstrates how to register a custom template loader using the `register_template_loaders` hook. It defines a `my_template_loader` function that returns an `llm.Template` object, showing how to fetch and structure template content, and handle potential errors.

```python
import llm

@llm.hookimpl
def register_template_loaders(register):
    register("my-prefix", my_template_loader)

def my_template_loader(template_path: str) -> llm.Template:
    """
    Documentation for the template loader goes here. It will be displayed
    when users run the 'llm templates loaders' command.
    """
    try:
        # Your logic to fetch the template content
        # This is just an example:
        prompt = "This is a sample prompt for {}".format(template_path)
        system = "You are an assistant specialized in {}".format(template_path)

        # Return a Template object with the required fields
        return llm.Template(
            name=template_path,
            prompt=prompt,
            system=system,
        )
    except Exception as e:
        # Raise a ValueError with a clear message if the template cannot be found
        raise ValueError(f"Template '{template_path}' could not be loaded: {str(e)}")
```

--------------------------------

### Specify LLM Models with Short Names

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The method for selecting specific models has been updated, replacing the `-4/--gpt4` option. Users can now specify models using `-m` followed by a short name like `4` or `gpt4`, leveraging a new short-name mechanism.

```Shell
llm -m 4
llm -m gpt4
```

--------------------------------

### Save an API Key (llm keys set)

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Saves a new API key or updates an existing one in the `keys.json` file. The key value can be provided interactively after running the command or directly via the `--value` option.

```Shell
Usage: llm keys set [OPTIONS] NAME

  Save a key in the keys.json file

  Example usage:

      $ llm keys set openai
      Enter key: ...

Options:
  --value TEXT  Value to set
  -h, --help    Show this message and exit.
```

--------------------------------

### Streaming Asynchronous LLM Responses (Python)

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Illustrates how to stream responses from an asynchronous LLM model using an `async for` loop, allowing for real-time processing of generated content.

```python
async for chunk in model.prompt(
    "Five surprising names for a pet pelican"
):
    print(chunk, end="", flush=True)
```

--------------------------------

### Extract Video Frames for Vision Models with llm-video-frames

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-video-frames plugin uses `ffmpeg` to convert a video file into a sequence of JPEG frames. These frames can then be fed into a vision model that does not natively support video inputs, enabling analysis of video content. The command specifies the video file and a prompt for describing key scenes.

```Shell
llm -f video-frames:video.mp4 'describe the key scenes in this video'
```

--------------------------------

### Defining LLM Schemas with Concise DSL Syntax

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

LLM provides a concise Domain Specific Language (DSL) for defining JSON schemas, simplifying manual construction. This DSL supports specifying property names, data types (string, int, float, bool), and descriptive hints for each field. Schemas can be defined on a single line or across multiple lines for improved readability and to allow commas within descriptions.

```APIDOC
name, bio
```

```APIDOC
name, bio, age int
```

```APIDOC
name: the person's name, age int: their age, bio: a short bio
```

```APIDOC
name: the person's name
age int: their age
bio: a short bio, no more than three sentences
```

--------------------------------

### Enable Logging for a Single LLM Prompt When Default is Off

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

Even if default logging is disabled, this command forces `llm` to log a specific prompt and its response. This allows selective logging without changing the global setting.

```bash
llm 'Five ambitious names for a pet pterodactyl' --log
```

--------------------------------

### View Recent LLM Logs

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

This command displays the three most recent logged items, including both prompts and responses, formatted in Markdown. It's a quick way to review recent interactions.

```bash
llm logs
```

--------------------------------

### Python API: llm.Collection Class

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Documents the new `llm.Collection` class for creating and searching collections of embeddings directly from Python code.

```APIDOC
llm.Collection
  Purpose: Class for creating and searching collections of embeddings.
  Usage: Used to manage and query embedding data programmatically.
```

--------------------------------

### Configuring Batch Size for LLM Embeddings

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Details options for controlling the batch size during embedding processing. This includes a command-line option for `llm embed-multi` and a programmatic argument for the `collection.embed_multi()` method, useful for optimizing memory usage.

```bash
llm embed-multi --batch-size 100
```

```Python
collection.embed_multi(batch_size=int)
```

--------------------------------

### Provide Cohere Generate and Summarize Models with llm-cohere

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-cohere plugin, by Alistair Shepherd, provides `cohere-generate` and `cohere-summarize` API models, powered by Cohere. It extends LLM with Cohere's text generation and summarization capabilities.

```APIDOC
Plugin: llm-cohere
  API Provider: Cohere
  Models Supported: cohere-generate, cohere-summarize
  Purpose: Integrates Cohere's generation and summarization API models.
```

--------------------------------

### Specify a different model for llm prompts

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Selects a specific language model, such as `gpt-4o`, for a prompt using the `-m` flag. This overrides the default model configured for `llm`.

```bash
llm 'Ten names for cheesecakes' -m gpt-4o
```

--------------------------------

### Use URL fragment in LLM prompt

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

Demonstrates how to include a fragment from a URL into an LLM prompt using the `-f` option. The content of the URL will be prepended to the prompt text sent to the model.

```bash
llm -f https://llm.datasette.io/robots.txt "Explain this robots.txt file in detail"
```

--------------------------------

### Retrieve Stored Embeddings with llm similar

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

This command shows how to query for similar embeddings using `llm similar`. When content and metadata are stored during embedding, `llm similar` returns these alongside the ID and similarity score, providing rich context for search results.

```bash
llm similar phrases -c 'hound'
```

```json
{"id": "hound", "score": 0.8484683588631485, "content": "my happy hound", "metadata": {"name": "Hound"}}
```

--------------------------------

### Declaring Binary Content Support in LLM Embedding Models

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/writing-plugins.md

This Python snippet shows how to configure an `llm.EmbeddingModel` subclass to indicate support for binary content. By setting `supports_binary = True`, the model can accept Python bytestrings in its `embed_batch` method, potentially mixed with regular strings if `supports_text` is also true (which is default).

```python
class ClipEmbeddingModel(llm.EmbeddingModel):
    model_id = "clip"
    supports_binary = True
    supports_text= True
```

--------------------------------

### Calculate Embedding with llm embed using OpenAI Model

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Demonstrates how to calculate an embedding for a string using the `llm embed` command with a specified OpenAI model. Requires an OpenAI API key to be set.

```bash
llm embed -c 'This is some content' -m 3-small
```

--------------------------------

### Applying Saved LLM Schema Templates

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

Saved LLM schema templates can be conveniently applied to generate structured output using the `llm` command. The `--schema t:template_name` option applies the specified template for single-item generation, while `--schema-multi t:template_name` is used for generating multiple items conforming to the same schema. This streamlines the process of generating consistent, structured data.

```bash
llm --schema t:dog 'invent a dog'
```

```bash
llm --schema-multi t:dog 'invent three dogs'
```

--------------------------------

### Support Anthropic Claude Models with llm-anthropic Plugin

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-anthropic plugin adds support for Anthropic's Claude 3 family, 3.5 Sonnet, and future models. It facilitates interaction with Anthropic's powerful conversational AI APIs.

```APIDOC
Plugin: llm-anthropic
  API Provider: Anthropic
  Models Supported: Claude 3 family, 3.5 Sonnet, and beyond
  Purpose: Integrates Anthropic's Claude models for LLM use.
```

--------------------------------

### Import Hacker News Conversations as Fragments with llm-hacker-news

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-hacker-news plugin allows importing conversations from Hacker News as fragments into LLM. This enables users to summarize or analyze discussions from specific Hacker News threads using LLM's capabilities. The command takes the Hacker News item ID.

```Shell
llm -f hn:43615912 'summary with illustrative direct quotes'
```

--------------------------------

### Configuring Encoding for Bulk Embeddings

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Describes the new `--encoding` option for `llm embed-multi --files` command, allowing specification of file encoding and defaulting to `latin-1` fallback for `utf-8` failures.

```CLI
llm embed-multi --files --encoding <encoding_name>
```

--------------------------------

### Initialize an llm.Collection for Embeddings

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/python-api.md

Shows various ways to initialize an `llm.Collection` object for working with named groups of embeddings, including in-memory and persistent SQLite databases, and passing model ID or object.

```Python
import sqlite_utils
import llm

# This collection will use an in-memory database that will be
# discarded when the Python process exits
collection = llm.Collection("entries", model_id="3-small")

# Or you can persist the database to disk like this:
db = sqlite_utils.Database("my-embeddings.db")
collection = llm.Collection("entries", db, model_id="3-small")

# You can pass a model directly using model= instead of model_id=
embedding_model = llm.get_embedding_model("3-small")
collection = llm.Collection("entries", db, model=embedding_model)
```

--------------------------------

### Save LLM Prompt to a Template

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Save a given prompt directly to a named template for future reuse. This allows for quick storage of frequently used prompts.

```Shell
llm "prompt" --save template
```

--------------------------------

### Implementing a Custom Embedding Model Plugin with Sentence-Transformers

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/writing-plugins.md

This Python code demonstrates how to create an LLM plugin that integrates a new embedding model using the `sentence-transformers` library. It includes the `register_embedding_models` hook to register the model and the `SentenceTransformerModel` class, which extends `llm.EmbeddingModel` and implements the `embed_batch` method for processing text batches.

```python
import llm
from sentence_transformers import SentenceTransformer


@llm.hookimpl
def register_embedding_models(register):
    model_id = "sentence-transformers/all-MiniLM-L6-v2"
    register(SentenceTransformerModel(model_id, model_id), aliases=("all-MiniLM-L6-v2",))


class SentenceTransformerModel(llm.EmbeddingModel):
    def __init__(self, model_id, model_name):
        self.model_id = model_id
        self.model_name = model_name
        self._model = None

    def embed_batch(self, texts):
        if self._model is None:
            self._model = SentenceTransformer(self.model_name)
        results = self._model.encode(texts)
        return (list(map(float, result)) for result in results)
```

--------------------------------

### llm fragments list --help

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Lists all current fragments stored in the LLM database. It supports searching for fragments matching specific query strings, filtering to show only fragments with aliases, and outputting the list as JSON.

```APIDOC
Usage: llm fragments list [OPTIONS]

  List current fragments

Options:
  -q, --query TEXT  Search for fragments matching these strings
  --aliases         Show only fragments with aliases
  --json            Output as JSON
  -h, --help        Show this message and exit.
```

--------------------------------

### Registering Python Functions as LLM Tools

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-hooks.md

This snippet demonstrates how to register standard Python functions as tools for the LLM library using the `register_tools` hook. It shows how to define functions like `upper` and `count_char` and make them available, including specifying a custom tool name.

```python
import llm

def upper(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()

def count_char(text: str, character: str) -> int:
    """Count the number of occurrences of a character in a word."""
    return text.count(character)

@llm.hookimpl
def register_tools(register):
    register(upper)
    # Here the name= argument is used to specify a different name for the tool:
    register(count_char, name="count_character_in_word")
```

--------------------------------

### Check LLM Log Database Status

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

This command provides an overview of the current logging configuration and statistics. It shows whether logging is active, the database path, and the number of conversations and responses logged.

```bash
llm logs status
```

--------------------------------

### CLI: Managing and Extracting Log Entries

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm logs` command gains new options: `--short` (`-s`) for truncated YAML output without responses, and `--extract-last` (`-xl`) or `--extract` (`-x`) to extract the last or first fenced code block from matching log entries.

```Shell
llm logs --short
llm logs -s
llm logs --extract-last
llm logs -xl
llm logs --extract
llm logs -x
```

--------------------------------

### Converting LLM Schema DSL to JSON Schema via CLI

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

The `llm schemas dsl` command-line utility allows users to convert a concise LLM schema DSL string into its equivalent, fully-formed JSON schema representation. This is useful for validating the DSL syntax and understanding the underlying JSON structure generated by LLM. The output provides a standard JSON schema object, including property types and required fields.

```bash
llm schemas dsl 'name, age int'
```

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "age": {
      "type": "integer"
    }
  },
  "required": [
    "name",
    "age"
  ]
}
```

--------------------------------

### LLM Plugin Hook: register_models

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

Documentation for the `register_models` plugin hook, used to register model instances (sync and async) with the LLM framework.

```APIDOC
@llm.hookimpl
def register_models(register):
  Purpose: Plugin hook to register model instances with LLM.
  Parameters:
    register (callable): A function to call with model instances and optional aliases.
  Usage:
    register(MyModel(), MyAsyncModel(), aliases=("my-model-aliases",))
```

--------------------------------

### Access Together AI Hosted Models with llm-together Plugin

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-together plugin adds support for the Together AI extensive family of hosted openly licensed models. It allows LLM to leverage a wide array of open-source models from Together AI.

```APIDOC
Plugin: llm-together
  API Provider: Together AI
  Models Supported: Extensive family of hosted openly licensed models
  Purpose: Integrates models from Together AI.
```

--------------------------------

### Retrieving a List of All Available Asynchronous LLM Models

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Demonstrates how to use `llm.get_async_models()` to specifically list models that support asynchronous operations. This helps in identifying models suitable for non-blocking applications and concurrent processing.

```python
for model in llm.get_async_models():
    print(model.model_id)
```

--------------------------------

### Explicitly Pass API Key to Model Prompt

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Learn to provide an API key directly to the `model.prompt()` method using the `key=` parameter. This is an alternative to environment variables or saved keys for authentication.

```python
model = llm.get_model("gpt-4o-mini")
print(model.prompt("Names for beavers", key="sk-..."))
```

--------------------------------

### Define JSON Schema with Python Dictionary

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Explore how to directly pass a Python dictionary representing a JSON schema to the `model.prompt()` method. This provides granular control over the structure and types of the LLM's generated output.

```python
response = model.prompt("Describe a nice dog", schema={
    "properties": {
        "name": {"title": "Name", "type": "string"},
        "age": {"title": "Age", "type": "integer"}
    },
    "required": ["name", "age"],
    "title": "Dog",
    "type": "object"
})
```

--------------------------------

### Debugging OpenAI API Responses (No-Stream) - Bash

Source: https://github.com/simonw/llm/blob/main/docs/contributing.md

Enables detailed logging of OpenAI API requests and responses without streaming the output, providing a more readable body for debugging purposes. This is useful for inspecting the full response at once.

```bash
LLM_OPENAI_SHOW_RESPONSES=1 llm -m chatgpt --no-stream \
  'three word slogan for an an otter-run bakery'
```

--------------------------------

### Python: Tracking Token Usage with response.set_usage()

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

The `response.set_usage()` method allows `llm` plugin developers to record token consumption. It accepts `input` and `output` integers for token counts, and an optional `details` dictionary for additional information like cached tokens. This data is logged and accessible via the Python API.

```python
response.set_usage(input=15, output=340, details={"cached": 37})
```

--------------------------------

### Define and Override Default Parameters in LLM YAML Templates

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

This snippet shows how to embed default parameter values directly within a YAML template using the `defaults:` key. It then illustrates how the template will use these defaults when executed without explicit parameters, and how these defaults can be easily overridden at runtime using the `-p/--param` option. This provides flexibility for template usage.

```YAML
system: Summarize this text in the voice of $voice
defaults:
  voice: GlaDOS
```

```Bash
curl -s 'https://til.simonwillison.net/macos/imovie-slides-and-audio' | \
  strip-tags -m | llm -t summarize
```

```Bash
curl -s 'https://til.simonwillison.net/macos/imovie-slides-and-audio' | \
  strip-tags -m | llm -t summarize -p voice Yoda
```

--------------------------------

### Filtering similar embeddings by ID prefix

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Demonstrates how to use the `--prefix` option with `llm similar` to filter search results and only show IDs that begin with a specific prefix. This helps narrow down searches to relevant subsets of embeddings.

```bash
llm similar quotations --prefix 'movies/' -c 'star wars'
```

--------------------------------

### Auto-Enable Plugin Tools on Conversation Continue

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

When continuing a conversation using `llm prompt` or `llm chat` with the `-c` or `--cid` options, plugin-provided tools are now automatically re-enabled, ensuring a seamless continuation of tool-assisted interactions.

```CLI
llm prompt -c <conversation_id>
llm chat --cid <conversation_id>
```

--------------------------------

### Set Default Option for an LLM Model

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Configures a default option (key-value pair) for a specified LLM model. This allows users to pre-set parameters like temperature for a model.

```Shell
Usage: llm models options set [OPTIONS] MODEL KEY VALUE

  Set a default option for a model

  Example usage:

      llm models options set gpt-4o temperature 0.5

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Attachment Object API Reference

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

Reference documentation for the `Attachment` object, which represents user-provided files or URLs. It details the properties available for accessing attachment metadata and content, and methods for resolving content type and retrieving binary or base64-encoded data.

```APIDOC
Attachment Object:
  Properties:
    url (str): The URL of the attachment, if provided as a URL.
    path (str): The resolved file path of the attachment, if provided as a file.
    type (str): The content type of the attachment, if provided.
    content (bytes): The binary content of the attachment, if provided.
  Methods:
    resolve_type() -> str:
      Returns the 'type' if available, otherwise attempts to guess the type by looking at the first few bytes of content.
    content_bytes() -> bytes:
      Returns the binary content, which may be read from a file or fetched from a URL.
    base64_content() -> str:
      Returns the content as a base64-encoded string.
    id() -> str:
      Returns a database ID for this content (SHA256 hash of binary content or hash of {"url": url}). This is an implementation detail which you should not need to access directly.
```

--------------------------------

### Support DeepSeek-Chat and DeepSeek-Coder with llm-deepseek

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-deepseek plugin adds support for DeepSeek's DeepSeek-Chat and DeepSeek-Coder models. It enables LLM to interact with DeepSeek's specialized conversational and coding models.

```APIDOC
Plugin: llm-deepseek

```

--------------------------------

### List Embedding Collections from Specific Database with llm CLI

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Use the `-d` or `--database` option to specify an alternative database file from which to list embedding collections. This allows managing collections across different database instances.

```bash
llm collections list -d my-embeddings.db
```

--------------------------------

### Uninstalling a Broken LLM Plugin

Source: https://github.com/simonw/llm/blob/main/docs/plugins/tutorial-model-plugin.md

This command demonstrates how to uninstall a problematic `llm` plugin, like `llm-markov`, by first disabling all plugin loading using the `LLM_LOAD_PLUGINS` environment variable. This ensures the `llm uninstall` command can execute successfully even if the plugin itself is causing errors.

```bash
LLM_LOAD_PLUGINS='' llm uninstall llm-markov
```

--------------------------------

### Edit an LLM Prompt Template

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Opens the specified prompt template in the default text editor (`$EDITOR`) for modification. This provides a convenient way to update template content.

```Shell
Usage: llm templates edit [OPTIONS] NAME

  Edit the specified prompt template using the default $EDITOR

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Manage Embedding Models with `llm embed-models` Command

Source: https://github.com/simonw/llm/blob/main/docs/help.md

The `llm embed-models` command provides subcommands for managing available embedding models. It allows users to list all registered models and to show or set the default embedding model for subsequent operations.

```Shell
Usage: llm embed-models [OPTIONS] COMMAND [ARGS]...

  Manage available embedding models

Options:
  -h, --help  Show this message and exit.

Commands:
  list*    List available embedding models
  default  Show or set the default embedding model
```

--------------------------------

### Show full content of a specific LLM fragment

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

Explains how to retrieve and display the complete content of a stored fragment using its hash ID with the `llm fragments show` command. This is useful for reviewing full fragment text.

```bash
llm fragments show 0d6e368f9bc21f8db78c01e192ecf925841a957d8b991f5bf9f6239aa4d81815
```

--------------------------------

### Viewing the LLM Aliases File Path (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/aliases.md

This command displays the file path where LLM stores its model aliases. This is useful for locating the `aliases.json` configuration file on the system.

```bash
llm aliases path
```

--------------------------------

### Filtering LLM Logs by Prompt Fragments

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

Filter `llm` command logs by prompt fragments using the `-f` or `--fragment` option. The `--expand` flag can be used to display full fragment content instead of just hash IDs.

```bash
llm logs -f https://llm.datasette.io/robots.txt --expand
```

--------------------------------

### Define a KeyModel for API Key Integration in LLM Plugins

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

This snippet demonstrates how to subclass `llm.KeyModel` to enable standard API key management for your LLM model plugin. It shows how to specify the required key identifier (`needs_key`) and an optional environment variable name (`key_env_var`) for key lookup.

```Python
import llm

class HostedModel(llm.KeyModel):
    needs_key = "hosted" # Required
    key_env_var = "HOSTED_API_KEY" # Optional
```

--------------------------------

### Embedding data from SQLite (attached database)

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Explains how to embed data from an external SQLite database by attaching it using `--attach` and referencing tables with aliases. This allows you to store embeddings in one database while sourcing content from another.

```bash
llm embed-multi docs \
  -d embeddings.db \
  --attach other other.db \
  --sql 'select id, title, content from other.documents' \
  -m 3-small
```

--------------------------------

### Store Embedding from Standard Input in SQLite Collection

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Shows how to pipe content from a file to `llm embed` to store its embedding in a specified collection under a given key. This is useful for batch processing files.

```bash
cat one.txt | llm embed files one
```

--------------------------------

### Access Google Gemini Models via llm-gemini Plugin

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-gemini plugin provides support for Google's Gemini models, allowing LLM users to leverage Google's advanced AI capabilities through a dedicated integration.

```APIDOC
Plugin: llm-gemini
  API Provider: Google
  Models Supported: Gemini models
  Purpose: Provides access to Google's Gemini models.
```

--------------------------------

### List LLM fragments with assigned aliases

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

Explains how to view only those fragments that have been assigned aliases using the `llm fragments --aliases` command. This provides a quick overview of aliased fragments.

```bash
llm fragments --aliases
```

--------------------------------

### CLI: Log Asynchronous Prompt Responses

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This command ensures that responses from asynchronous `llm prompt` operations are properly logged to the database. It is essential for maintaining a complete history of interactions, including those performed asynchronously.

```CLI
llm prompt ... --async
```

--------------------------------

### Generate Schema-Based JSON Data with llm

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

This snippet demonstrates how to use the 'llm' command with the '--schema-multi' option to generate and log multiple JSON objects based on a specified schema (e.g., 'name' and 'ten_word_bio'). This process creates entries in the 'llm' log database that can later be queried.

```bash
llm --schema-multi 'name, ten_word_bio' 'invent 3 cool dogs'
llm --schema-multi 'name, ten_word_bio' 'invent 2 cool dogs'
```

--------------------------------

### Using an LLM Model Alias for Generation (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/aliases.md

This command demonstrates how to use a previously defined alias (`mini`) to invoke a language model for text generation. The `-m` flag specifies the model alias to be used for the prompt.

```bash
llm -m mini 'An epic Greek-style saga about a cheesecake that builds a SQL database from scratch'
```

--------------------------------

### Support Anyscale Endpoints Models with llm-anyscale-endpoints

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-anyscale-endpoints plugin supports models hosted on the Anyscale Endpoints platform, including Llama 2 70B. It allows LLM to utilize models deployed on Anyscale.

```APIDOC
Plugin: llm-anyscale-endpoints
  API Provider: Anyscale Endpoints
  Models Supported: Models hosted on Anyscale Endpoints (e.g., Llama 2 70B)
  Purpose: Integrates models from the Anyscale Endpoints platform.
```

--------------------------------

### Check Logging Status (llm logs status)

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Displays the current status of database logging for `llm` prompts and responses. This command indicates whether logging is currently enabled or disabled.

```Shell
Usage: llm logs status [OPTIONS]

  Show current status of database logging

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Support Fireworks AI Hosted Models with llm-fireworks

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-fireworks plugin supports models hosted by Fireworks AI. It enables LLM to interact with models provided by Fireworks AI for various generative tasks.

```APIDOC
Plugin: llm-fireworks
  API Provider: Fireworks AI
  Models Supported: Models hosted by Fireworks AI
  Purpose: Integrates models from Fireworks AI.
```

--------------------------------

### Save Schemas to Prompt Templates (CLI)

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Command to save a specified schema to a named prompt template for reuse.

```Bash
llm --schema X --save template-name
```

--------------------------------

### Fix: pathlib.Path Handling in llm templates edit

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Addressed a bug in `llm templates edit` where `pathlib.Path` objects were not correctly cast to strings before being passed to `click.edit`, preventing potential errors when editing templates.

```Python
str(pathlib.Path_object) # Ensure string conversion before passing to click.edit
```

--------------------------------

### Implement `before_call` Hook for Tool Call Validation

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Demonstrates how to use the `before_call` parameter in `model.chain()` to execute a function before each tool call. This hook receives the `llm.Tool` and `llm.ToolCall` objects, allowing for inspection and conditional cancellation of tool execution by raising `llm.CancelToolCall`.

```Python
import llm
from typing import Optional

def upper(text: str) -> str:
    "Convert text to uppercase."
    return text.upper()

def before_call(tool: Optional[llm.Tool], tool_call: llm.ToolCall):
    print(f"About to call tool {tool.name} with arguments {tool_call.arguments}")
    if tool.name == "upper" and "bad" in repr(tool_call.arguments):
        raise llm.CancelToolCall("Not allowed to call upper on text containing 'bad'")

model = llm.get_model("gpt-4.1-mini")
response = model.chain(
    "Convert panda to upper and badger to upper",
    tools=[upper],
    before_call=before_call,
)
print(response.text())
```

--------------------------------

### Listing LLM Model Aliases as JSON (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/aliases.md

This command lists all currently configured model aliases in the LLM tool, formatted as a JSON object. This is particularly useful for programmatic access or integration with other scripts and applications.

```bash
llm aliases list --json
```

--------------------------------

### Managing LLM Model Aliases via CLI

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm aliases` command suite allows users to configure, list, and remove custom aliases for LLM models directly from the command line. This simplifies using long model IDs by assigning shorter, more memorable names, enhancing usability for frequent model interactions.

```bash
llm aliases set turbo gpt-3.5-turbo-16k
llm -m turbo 'An epic Greek-style saga about a cheesecake that builds a SQL database from scratch'
llm aliases list
llm aliases remove turbo
```

--------------------------------

### Use fragment alias in LLM prompt

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

Demonstrates how to use a previously defined alias instead of a hash ID or path when specifying a fragment with the `-f` option. This simplifies prompt construction for common fragments.

```bash
llm -f mydocs 'How do I access metadata?'
```

--------------------------------

### Truncate and Output Single LLM Log Entry as JSON

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

This command combines truncation with JSON output for a single log entry. The `-t` flag shortens prompts and responses, improving readability for detailed JSON output.

```bash
llm logs -n 1 -t --json
```

--------------------------------

### Retrieve Similar Items using Query String

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/python-api.md

Illustrates how to use the `collection.similar()` method to find items most similar to a given query string. This method performs a brute-force distance calculation, suitable for small collections. The `entry` object returned includes `id`, `score`, `content`, and `metadata`.

```python
for entry in collection.similar("hound"):
    print(entry.id, entry.score)
```

```python
for entry in collection.similar("hound", number=5):
    print(entry.id, entry.score)
```

--------------------------------

### Set Default OpenAI API Key for LLM

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This command prompts the user to securely set the default API key for OpenAI services within the LLM tool. Once set, this key will be used for all subsequent OpenAI API calls unless overridden.

```bash
llm keys set openai
```

--------------------------------

### Embed Text with `llm embed` Command

Source: https://github.com/simonw/llm/blob/main/docs/help.md

The `llm embed` command is used to generate and store embeddings for a single piece of text. It supports various input sources like files or direct content, allows specifying the embedding model, and offers options to store the original text or format the output.

```Shell
Usage: llm embed [OPTIONS] [COLLECTION] [ID]

  Embed text and store or return the result

Options:
  -i, --input PATH                File to embed
  -m, --model TEXT                Embedding model to use
  --store                         Store the text itself in the database
  -d, --database FILE
  -c, --content TEXT              Content to embed
  --binary                        Treat input as binary data
  --metadata TEXT                 JSON object metadata to store
  -f, --format [json|blob|base64|hex]
                                  Output format
  -h, --help                      Show this message and exit.
```

--------------------------------

### Access OpenRouter Hosted Models via llm-openrouter Plugin

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-openrouter plugin provides access to models hosted on OpenRouter. It allows LLM to utilize a wide range of models available through the OpenRouter platform.

```APIDOC
Plugin: llm-openrouter
  API Provider: OpenRouter
  Models Supported: Models hosted on OpenRouter
  Purpose: Provides access to a variety of models via OpenRouter.
```

--------------------------------

### Python API: Accessing Response Data and Usage

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `response` object now provides `response.json()` and `response.usage()` methods for accessing the underlying JSON data and usage statistics of a model's response, respectively.

```APIDOC
llm.Response:
  Object representing a model's response.
  Methods:
    json(): dict - Returns the underlying JSON data of the response.
    usage(): dict - Returns usage statistics for the response.
```

--------------------------------

### Searching for similar embeddings with text query

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Demonstrates how to use `llm similar` to find items semantically similar to a given text string in an embedding collection. The command embeds the provided string and returns a newline-delimited list of JSON objects.

```bash
llm similar quotations -c 'computer science'
```

--------------------------------

### llm chat Respects Default Model Options

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm chat` command now correctly applies default model options that have been configured using `llm models set-options`, ensuring consistent model behavior across chat sessions.

```CLI
llm models set-options gpt-4o --option value
llm chat
```

--------------------------------

### Continue Most Recent Chat Conversation

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Shows how to continue the most recent chat conversation using the `-c` flag with `llm chat`. This automatically re-uses the model from the previous session, allowing for seamless continuation of dialogue.

```bash
llm chat -c
```

--------------------------------

### Convert LLM Schema DSL to JSON Schema

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Converts LLM's domain-specific language (DSL) for schemas into a standard JSON schema format. This is useful for integrating LLM schemas with other systems that expect JSON schema.

```Shell
Usage: llm schemas dsl [OPTIONS] INPUT

  Convert LLM's schema DSL to a JSON schema

      llm schema dsl 'name, age int, bio: their bio'

Options:
  --multi     Wrap in an array
  -h, --help  Show this message and exit.
```

--------------------------------

### Store Embedding in Named SQLite Collection with llm embed

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Demonstrates how to store a text embedding in a named SQLite collection using `llm embed`, specifying both the collection name and a unique key for the content. Collections group embeddings by model.

```bash
llm embed quotations philkarlton-1 -c \n  'There are only two hard things in Computer Science: cache invalidation and naming things'
```

--------------------------------

### Custom OpenAI Model Configuration YAML

Source: https://github.com/simonw/llm/blob/main/docs/openai-models.md

This YAML snippet demonstrates how to add a new OpenAI model, `gpt-3.5-turbo-0613`, to LLM's configuration. It specifies the `model_id`, `model_name`, and optional `aliases`. Additional properties like `completion`, `supports_schema`, and `reasoning` can be included based on the model's capabilities.

```yaml
- model_id: gpt-3.5-turbo-0613
  model_name: gpt-3.5-turbo-0613
  aliases: ["0613"]
```

--------------------------------

### View Expanded Fragments for Recent Conversation

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

This command displays the full content of fragments used in your most recent `llm` conversation. It utilizes the `-c` option for the most recent conversation and `--expand` to show the complete fragment content instead of just hash IDs.

```bash
llm logs -c --expand
```

--------------------------------

### OpenAI Plugin: Reconstructing Conversation History with Attachments

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

This Python snippet illustrates how the OpenAI plugin reconstructs the `messages` list for continuing a conversation, incorporating attachments from previous user prompts and assistant responses. It iterates through `conversation.responses`, using the `_attachment` helper (defined elsewhere) to re-add attachment data and `response.text_or_raise()` to retrieve assistant text.

```python
for prev_response in conversation.responses:
    if prev_response.attachments:
        attachment_message = []
        if prev_response.prompt.prompt:
            attachment_message.append(
                {"type": "text", "text": prev_response.prompt.prompt}
            )
        for attachment in prev_response.attachments:
            attachment_message.append(_attachment(attachment))
        messages.append({"role": "user", "content": attachment_message})
    else:
        messages.append(
            {"role": "user", "content": prev_response.prompt.prompt}
        )
    messages.append({"role": "assistant", "content": prev_response.text_or_raise()})
```

--------------------------------

### Set Default Model Option in LLM CLI

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Configures a default option for a specific model, such as setting the temperature for 'gpt-4o'. This option will be applied automatically when running prompts through that model.

```bash
llm models options set gpt-4o temperature 0.5
```

--------------------------------

### Retrieving LLM Token Usage Statistics (Python)

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Illustrates how to access token usage details for a model response using the `response.usage()` method. The `Usage` object provides `.input` and `.output` properties for token counts, and a `.details` dictionary for additional, model-specific information.

```python
pprint(response.usage())
```

```python
Usage(input=5,
      output=2,
      details={'candidatesTokensDetails': [{'modality': 'TEXT',
                                            'tokenCount': 2}],
               'promptTokensDetails': [{'modality': 'TEXT', 'tokenCount': 5}]})
```

--------------------------------

### Store Embedding with Explicit Model and Collection Name

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Illustrates storing an embedding in a specific collection with a defined key and explicitly chosen model, overriding any default settings. This provides fine-grained control over embedding storage.

```bash
llm embed phrases hound -m 3-small -c 'my happy hound'
```

--------------------------------

### Store Embedding in Custom SQLite Database File

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Explains how to store embeddings in a SQLite database file other than the default `embeddings.db` by using the `-d/--database` option. This allows for managing multiple embedding databases.

```bash
llm embed phrases hound -d my-embeddings.db -c 'my happy hound'
```

--------------------------------

### Register Custom Template Loaders in LLM Plugins

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

An experimental `register_template_loaders()` plugin hook has been introduced in `llm`. This enables developers to register custom functions for loading templates, providing flexibility in how prompts and other structured inputs are managed.

```Python
from llm.plugins import register_template_loaders

@register_template_loaders
def my_template_loader(template_name: str):
    # Custom logic to load a template by name
    return "This is my custom template for {input}."
```

--------------------------------

### Pipe an attachment with explicit content type to llm

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Pipes an attachment and explicitly specifies its content type using `--attachment-type` (`--at`). This ensures correct processing when automatic type detection might fail.

```bash
cat myfile | llm "describe this image" --at - image/jpeg
```

--------------------------------

### LLM Plugin Tooling API Reference

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

This section provides the API definitions for `llm.Tool`, `llm.ToolCall`, and `llm.ToolResult` dataclasses, which are essential for implementing tool support in LLM model plugins. These classes define the structure for tools available to the model, calls made by the model, and the results of those tool calls.

```APIDOC
llm.Tool
llm.ToolCall
llm.ToolResult
```

--------------------------------

### Specifying custom encodings for file embedding

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Illustrates how to use the `--encoding` option multiple times to specify a fallback sequence of character encodings for files during embedding. This ensures robust handling of files with various character sets, preventing read errors.

```bash
llm embed-multi documentation \
  -m 3-small \
  --files docs '**/*.md' \
  -d documentation.db \
  --encoding utf-16 \
  --encoding mac_roman \
  --encoding latin-1
```

--------------------------------

### Outputting Last LLM Response with llm logs

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Illustrates the use of the `-r` or `--response` option with the `llm logs` command to retrieve only the last captured LLM response, without additional Markdown wrapping or accompanying prompt.

```Shell
llm logs --response
```

--------------------------------

### Fix: Tool Plugin Name Parameter Ignored

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Resolved a bug where the `name` parameter provided in the `register(function, name="name")` call for tool plugins was being ignored, ensuring that custom tool names are now correctly applied.

```APIDOC
register(function, name="custom_tool_name") # 'name' parameter now respected
```

--------------------------------

### Configure Code Extraction for LLM Templates

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

This snippet demonstrates how to enable automatic extraction of the first fenced code block from the LLM's output within a template. By adding `extract: true` to the YAML template, the `llm` tool will process the output to isolate and return only the code block, which is useful for generating executable code.

```YAML
extract: true
```

--------------------------------

### Access Reka AI Models with llm-reka Plugin

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-reka plugin provides support for the Reka family of models through their API. It enables LLM to interact with Reka's AI offerings.

```APIDOC
Plugin: llm-reka
  API Provider: Reka AI
  Models Supported: Reka family of models
  Purpose: Integrates Reka AI models via their API.
```

--------------------------------

### Manage Embedding Collections with `llm collections` Command

Source: https://github.com/simonw/llm/blob/main/docs/help.md

The `llm collections` command provides utilities for viewing and managing collections of embeddings. It includes subcommands to list all existing collections, delete a specific collection, and output the file path to the embeddings database.

```Shell
Usage: llm collections [OPTIONS] COMMAND [ARGS]...

  View and manage collections of embeddings

Options:
  -h, --help  Show this message and exit.

Commands:
  list*   View a list of collections
  delete  Delete the specified collection
  path    Output the path to the embeddings database
```

--------------------------------

### Shorten LLM Log Output to Include Prompt End

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm logs` command's short output option (`-s` or `--short`) has been improved to ensure that the end of the prompt is included in the truncated display, providing better context.

```Bash
llm logs --short
```

--------------------------------

### Manage LLM Logging Database Status

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Control and view the logging behavior of the `llm` tool. Logging can be turned off, turned on, or its current status can be checked.

```Shell
llm logs off
llm logs on
llm logs status
```

--------------------------------

### Check for Configured Default LLM Model

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

This pattern demonstrates how to use the `default` parameter with `llm.get_default_model()` to determine if a default model has been explicitly configured. If `default=None` is passed and no default is set, the function returns `None`.

```Python
if llm.get_default_model(default=None) is None:
    print("No default has been set")
```

--------------------------------

### Implement `after_call` Hook for Tool Call Logging

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Illustrates the use of the `after_call` parameter in `model.chain()` to run a logging function after a tool call has completed. This hook provides access to the `llm.Tool`, `llm.ToolCall`, and `llm.ToolResult` objects, enabling post-execution monitoring and debugging.

```Python
def after_call(tool: llm.Tool, tool_call: llm.ToolCall, tool_result: llm.ToolResult):
    print(f"Tool {tool.name} called with arguments {tool_call.arguments} returned {tool_result.output}")

response = model.chain(
    "Convert panda to upper and badger to upper",
    tools=[upper],
    after_call=after_call,
)
print(response.text())
```

--------------------------------

### Executing Callback Functions Upon LLM Response Completion (Synchronous)

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Shows how to use the `response.on_done(callback)` method to execute a function once an LLM response has fully completed. This is useful for post-processing tasks like tracking token usage, logging, or triggering subsequent actions.

```python
import llm

model = llm.get_model("gpt-4o-mini")
response = model.prompt("a poem about a hippo")
response.on_done(lambda response: print(response.usage()))
print(response.text())
```

--------------------------------

### Optional Prompt String in LLM Python API

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Demonstrates that the prompt string is now optional when calling `model.prompt()` from the Python API, allowing calls with only attachments.

```Python
model.prompt(attachments=llm.Attachment(url=url))
```

--------------------------------

### Integrating Synchronous and Asynchronous Tool Functions with LLM (Python)

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Explains that LLM supports both synchronous and asynchronous (`async def`) tool functions. It highlights LLM's capability to automatically execute `async def` functions in a thread pool within a synchronous context using `asyncio.run()`, ensuring compatibility.

```python
async def hello(name: str) -> str:
    "Say hello to name"
    return "Hello there " + name

model = llm.get_model("gpt-4.1-mini")
chain_response = model.chain(
    "Say hello to Percival", tools=[hello]
)
print(chain_response.text())
```

--------------------------------

### Output Expanded Fragments in JSON Format

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

This command retrieves the most recent `llm` conversation logs and outputs them in JSON format. The `--expand` option ensures that the full content of each fragment is included in the JSON output, rather than just truncated IDs.

```bash
llm logs -c --json --expand
```

--------------------------------

### Set a Default Model for an LLM Template

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

This snippet shows how to specify a default language model for a particular `llm` template using the `model:` key in its YAML definition. This ensures that the template always uses the desired model (e.g., `gpt-4o`) regardless of the user's global default, providing consistent behavior for specialized prompts.

```YAML
model: gpt-4o
system: roast the user at every possible opportunity, be succinct
```

```Bash
llm -t roast 'How are you today?'
```

--------------------------------

### Filter llm logs by Tool Usage

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm logs` command now provides options to filter log entries based on tool usage. Use `--tool <name>` to show responses involving a specific tool, or `--tools` to display all responses that utilized any tool.

```CLI
llm logs --tool simple_eval
llm logs --tools
```

--------------------------------

### Store Multiple Embeddings in Bulk Using embed_multi

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/python-api.md

Shows how to efficiently store embeddings for multiple items at once in an `llm.Collection` using `collection.embed_multi()`, with an option to store content.

```Python
collection.embed_multi(
    [
        ("hound", "my happy hound"),
        ("cat", "my dissatisfied cat"),
    ],
    # Add this to store the strings in the content column:
    store=True,
)
```

--------------------------------

### Adding an LLM Alias Using Search Terms (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/aliases.md

This command sets a new alias by searching for a model matching the provided query terms. The `mini` alias is set to the first model matching both '4o' and 'mini', useful when the exact model ID is not fully known.

```bash
llm aliases set mini -q 4o -q mini
```

--------------------------------

### Rename `llm chatgpt` to `llm prompt`

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm chatgpt` command has been renamed to `llm prompt` to better reflect its general purpose of generating prompts. Users should now use `llm prompt` for their prompt generation needs.

```Shell
llm prompt
```

--------------------------------

### Listing Available OpenAI Embedding Models in LLM

Source: https://github.com/simonw/llm/blob/main/docs/openai-models.md

This output displays the OpenAI embedding models supported by the LLM tool, along with their aliases. These models are used to generate vector embeddings for text, which can then be used for similarity searches or other machine learning tasks.

```bash
ada-002 (aliases: ada, oai)
3-small
3-large
3-small-512
3-large-256
3-large-1024
```

--------------------------------

### Streaming Chained Responses from Asynchronous LLM Models

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Illustrates how to iterate over the output of a chained response from an asynchronous model as it arrives. It uses an `async for` loop to process chunks of the response, providing a streaming experience for real-time output.

```python
async for chunk in model.chain(
    "Convert panda to uppercase then pelican to uppercase",
    tools=[upper]
):
    print(chunk, end="", flush=True)
```

--------------------------------

### Filtering LLM Logs by Used Tools

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

Filter `llm` command logs for responses that involved a result from specific tools using the `--tool` or `-T` option. Multiple tools can be specified to match responses that used all of them.

```bash
llm logs -T simple_eval
```

--------------------------------

### Embed with Metadata and Store Content in Collection

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/python-api.md

Illustrates how to store additional JSON-compatible metadata and the text content itself when embedding an item into an `llm.Collection` using `store=True` and `metadata=`.

```Python
collection.embed("hound", "my happy hound", metadata={"name": "Hound"}, store=True)
```

--------------------------------

### Use fragment hash ID in LLM prompt

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

Demonstrates how to reference a previously stored fragment by its SHA256 hash ID using the `-f` option. This allows for precise reuse of specific content.

```bash
llm -f 16b686067375182573e2aa16b5bfc1e64d48350232535d06444537e51f1fd60c 'Extract metadata'
```

--------------------------------

### Integrate Mistral AI Language and Embedding Models with llm-mistral

Source: https://github.com/simonw/llm/blob/main/docs/plugins/directory.md

The llm-mistral plugin enables interaction with Mistral AI's language and embedding models through their official API. It extends the LLM framework to support Mistral's offerings for text generation and embeddings.

```APIDOC
Plugin: llm-mistral
  API Provider: Mistral AI
  Models Supported: Language and embedding models
  Purpose: Integrates Mistral AI's API for LLM interactions.
```

--------------------------------

### Python API Error Handling for Unknown Models

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm.get_model` function is now explicitly documented to raise an `llm.UnknownModelError` if the requested model identifier does not correspond to an existing model. This clarifies the expected error behavior for API consumers, allowing for robust error handling.

```APIDOC
llm.get_model(model_id: str) -> llm.Model
  Raises: llm.UnknownModelError if model_id does not exist.
```

--------------------------------

### Search for Specific Embedding Models with llm CLI

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Use the `-q` option with `llm embed-models` to filter and search for embedding models matching one or more specified terms. This is useful for quickly finding a specific model among many available options.

```bash
llm embed-models -q 3-small
```

--------------------------------

### Store Multiple Embeddings with Metadata in Bulk

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/python-api.md

Demonstrates using `collection.embed_multi_with_metadata()` to store multiple items along with their respective metadata, offering an option to store content.

```Python
collection.embed_multi_with_metadata(
    [
        ("hound", "my happy hound", {"name": "Hound"}),
        ("cat", "my dissatisfied cat", {"name": "Cat"}),
    ],
    # This can also take the store=True argument:
    store=True,
)
```

--------------------------------

### Extract People from Image Attachment using LLM

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

This command illustrates how to extract 'people' data from an image file using `llm`. It specifies the 'people' template, provides a URL to an image as an attachment (`-a`), and explicitly uses the 'gpt-4o' model (`-m`).

```bash
llm -t people -a https://static.simonwillison.net/static/2025/onion-zuck.jpg -m gpt-4o
```

--------------------------------

### Retrieve System-Wide Default LLM Model

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

The `llm.get_default_model()` function returns the currently configured default model. If no default has been explicitly set, it defaults to `gpt-4o-mini`.

```Python
import llm

model_id = llm.get_default_model()
```

--------------------------------

### Extract People from Web Article using LLM

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

This command demonstrates how to extract structured 'people' data from a web article using the `llm` tool. It pipes the content of a Guardian article, stripped of HTML tags, into `llm` using the predefined 'people' template.

```bash
curl https://www.theguardian.com/commentisfree/2025/feb/27/billy-mcfarland-new-fyre-festival-fantasist | \
  strip-tags | llm -t people
```

--------------------------------

### Extract Schema-Structured Data from LLM Logs (CLI)

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Options for the `llm logs` command to extract data collected using schemas, allowing filtering and specific key extraction from log entries.

```Bash
llm logs --data
```

```Bash
llm logs --data-key <key_name>
```

```Bash
llm logs --data-array
```

```Bash
llm logs --data-ids
```

--------------------------------

### Adding Attachments to LLM Conversation Prompts

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Demonstrates how to include attachments, such as images via URLs, when prompting within an `llm` conversation. This extends the conversational capabilities to include multimodal inputs, allowing the model to process external content.

```python
response = conversation.prompt(
    "Describe these birds",
    attachments=[
        llm.Attachment(url="https://static.simonwillison.net/static/2024/pelicans.jpg")
    ]
)
```

--------------------------------

### Load an Embedding Model in Python

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/python-api.md

Demonstrates how to load an embedding model using its model ID or alias with `llm.get_embedding_model()`.

```Python
import llm

embedding_model = llm.get_embedding_model("3-small")
```

--------------------------------

### Executing Callback Functions Upon LLM Response Completion (Asynchronous)

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Demonstrates how to use `response.on_done(callback)` with asynchronous models, requiring `await response.on_done(done)` to queue the callback. The callback itself can be an `async def` method, suitable for integration into asynchronous workflows.

```python
import asyncio, llm

async def run():
    model = llm.get_async_model("gpt-4o-mini")
    response = model.prompt("a short poem about a brick")
    async def done(response):
        print(await response.usage())
        print(await response.text())
    await response.on_done(done)
    print(await response.text())

asyncio.run(run())
```

--------------------------------

### View Logged Items as JSON Array

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

This command is similar to viewing newline-delimited logs, but it wraps all extracted 'items' into a single, valid JSON array. This is useful for applications that expect a single JSON document.

```bash
llm logs --schema t:people --data-key items --data-array
```

--------------------------------

### Streaming LLM Responses in Python

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Explains how to stream responses from LLM models as they are generated, iterating over the `response` object. The `response.text()` method internally performs this iteration to gather the full string.

```python
response = model.prompt("Five diabolical names for a pet goat")
for chunk in response:
    print(chunk, end="")
```

--------------------------------

### Sending Prompts within an Ongoing LLM Conversation

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Shows how to use the `conversation.prompt()` method to send prompts and receive responses within an established conversation. It highlights how the conversation context is preserved, allowing for follow-up questions based on previous interactions without re-specifying context.

```python
response = conversation.prompt("Five fun facts about pelicans")
print(response.text())
```

```python
response2 = conversation.prompt("Now do skunks")
print(response2.text())
```

--------------------------------

### Set alias for an LLM fragment

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

Shows how to assign a memorable alias to a fragment using the `llm fragments set` command. Aliases make it easier to reference frequently used fragments without their long hash IDs.

```bash
llm fragments set mydocs ./docs.md
```

--------------------------------

### Adding a New LLM Model Alias (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/aliases.md

This command sets a new alias for a specific model ID. The `mini` alias is created to refer to `gpt-4o-mini`, simplifying future model references and command line usage.

```bash
llm aliases set mini gpt-4o-mini
```

--------------------------------

### Python API: llm.get_embedding_model() Function

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Documents the `llm.get_embedding_model()` interface for directly embedding strings using Python.

```APIDOC
llm.get_embedding_model(model_name: str)
  Purpose: Interface for obtaining an embedding model instance.
  Parameters:
    model_name (str): The name of the embedding model to retrieve.
  Returns: An embedding model object capable of processing strings.
```

--------------------------------

### Filtering LLM Logs by Model

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

Filter `llm` command logs to display entries for a specific model or model alias using the `-m` or `--model` option.

```bash
llm logs -m chatgpt
```

--------------------------------

### Embed and Store a Single Item in a Collection

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/python-api.md

Demonstrates how to embed a single string and store it in an `llm.Collection` using the `collection.embed()` method, associating it with a key.

```Python
collection.embed("hound", "my happy hound")
```

--------------------------------

### Embed Multiple Strings Efficiently

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/python-api.md

Demonstrates using `embed_multi()` to process multiple strings at once, which can be more efficient for some models. It returns a generator yielding embedding vectors.

```Python
vectors = list(embedding_model.embed_multi(["my happy hound", "my dissatisfied cat"]))
```

--------------------------------

### Filter LLM Logs by ID (CLI)

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

New options for the `llm logs` command to filter entries based on their ID, using 'greater than' or 'greater than or equal to' conditions.

```Bash
llm logs --id-gt X
```

```Bash
llm logs --id-gte X
```

--------------------------------

### Set Chained Tool Execution Limit for llm prompt and chat

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Users can now control the maximum number of consecutive tool calls allowed within a single prompt or chat session using the `--chain-limit <N>` (or `--cl`) option for `llm prompt` and `llm chat`. The default limit is 5, with 0 indicating no limit.

```CLI
llm prompt --chain-limit 3
llm chat --cl 0
```

--------------------------------

### Embed Multiple Strings with `llm embed-multi` Command

Source: https://github.com/simonw/llm/blob/main/docs/help.md

The `llm embed-multi` command facilitates storing embeddings for multiple strings simultaneously within a specified collection. It supports diverse input formats including CSV, TSV, JSON, JSONL files, SQL queries against SQLite databases, and files from directories matching glob patterns.

```Shell
Usage: llm embed-multi [OPTIONS] COLLECTION [INPUT_PATH]

  Store embeddings for multiple strings at once in the specified collection.

  Input data can come from one of three sources:

  1. A CSV, TSV, JSON or JSONL file:
     - CSV/TSV: First column is ID, remaining columns concatenated as content
     - JSON: Array of objects with "id" field and content fields
     - JSONL: Newline-delimited JSON objects

     Examples:
       llm embed-multi docs input.csv
       cat data.json | llm embed-multi docs -
       llm embed-multi docs input.json --format json

  2. A SQL query against a SQLite database:
     - First column returned is used as ID
     - Other columns concatenated to form content

     Examples:
       llm embed-multi docs --sql "SELECT id, title, body FROM posts"
       llm embed-multi docs --attach blog blog.db --sql "SELECT id, content FROM blog.posts"

  3. Files in directories matching glob patterns:
     - Each file becomes one embedding
     - Relative file paths become IDs

     Examples:
       llm embed-multi docs --files docs '**/*.md'
       llm embed-multi images --files photos '*.jpg' --binary
       llm embed-multi texts --files texts '*.txt' --encoding utf-8 --encoding latin-1

Options:
  --format [json|csv|tsv|nl]   Format of input file - defaults to auto-detect
  --files <DIRECTORY TEXT>...  Embed files in this directory - specify directory
                               and glob pattern
  --encoding TEXT              Encodings to try when reading --files
  --binary                     Treat --files as binary data
  --sql TEXT                   Read input using this SQL query
  --attach <TEXT FILE>...      Additional databases to attach - specify alias
                               and file path
  --batch-size INTEGER         Batch size to use when running embeddings
  --prefix TEXT                Prefix to add to the IDs
  -m, --model TEXT             Embedding model to use
  --prepend TEXT               Prepend this string to all content before
                               embedding
  --store                      Store the text itself in the database
  -d, --database FILE
  -h, --help                   Show this message and exit.
```

--------------------------------

### Using llm logs for Conversation History

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm logs` command now outputs a readable Markdown format by default. Users can retrieve the old JSON format using the `--json` option or view specific conversation logs by providing a conversation ID with `--conversation ID` or `--cid ID`.

```bash
llm logs --json
llm logs --conversation ID
llm logs --cid ID
```

--------------------------------

### Embed Data from File with llm embed-multi

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

This command demonstrates how to use `llm embed-multi` to process data from a specified file. The first argument is the collection name, followed by the filename. LLM automatically detects the file format, but it can be explicitly set using the `--format` option for cases like newline-delimited JSON from standard input.

```bash
llm embed-multi items mydata.csv
```

```bash
cat mydata.json | llm embed-multi items -
```

```bash
cat mydata.json | llm embed-multi items - --format nl
```

--------------------------------

### Continue LLM Chat Conversation with Previous Context

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This command continues the most recent chat conversation using the `-c` or `--continue` option. It automatically includes the previous prompts and responses in the new request, allowing the model to maintain conversational context.

```bash
llm "What do you think of snacks?" -c
```

--------------------------------

### Find Similar Embeddings with `llm similar` Command

Source: https://github.com/simonw/llm/blob/main/docs/help.md

The `llm similar` command allows users to find the top N most similar IDs within a specified collection using cosine similarity. It can compare against new content provided directly or against an existing stored ID, offering options for input source, number of results, and output format.

```Shell
Usage: llm similar [OPTIONS] COLLECTION [ID]

  Return top N similar IDs from a collection using cosine similarity.

  Example usage:

      llm similar my-collection -c "I like cats"

  Or to find content similar to a specific stored ID:

      llm similar my-collection 1234

Options:
  -i, --input PATH      File to embed for comparison
  -c, --content TEXT    Content to embed for comparison
  --binary              Treat input as binary data
  -n, --number INTEGER  Number of results to return
  -p, --plain           Output in plain text format
  -d, --database FILE
  --prefix TEXT         Just IDs with this prefix
  -h, --help            Show this message and exit.
```

--------------------------------

### Input File Formats for llm embed-multi

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

This section illustrates the expected data formats for CSV, TSV, and JSON files when used as input for the `llm embed-multi` command. Each format requires an 'id' column and at least one content column for embedding. Newline-delimited JSON is also supported.

```csv
id,content
one,This is the first item
two,This is the second item
```

```json
[
  {"id": "one", "content": "This is the first item"},
  {"id": "two", "content": "This is the second item"}
]
```

```json
{"id": "one", "content": "This is the first item"}
{"id": "two", "content": "This is the second item"}
```

--------------------------------

### Insert fragments during LLM chat conversation

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

Shows how to dynamically add fragments to an ongoing LLM chat using the `!fragment <my_fragment>` command. This allows updating the chat context with new information mid-conversation.

```bash
!fragment https://llm.datasette.io/en/stable/fragments.html
```

--------------------------------

### List Embedding Collections in JSON Format with llm CLI

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Add the `--json` flag to the `llm collections list` command to receive the output in a structured JSON format. This is particularly useful for programmatic parsing and integration with other tools.

```bash
llm collections list --json
```

--------------------------------

### Use LLM Model Alias

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Use a predefined alias, such as `4-32k`, as a shorthand for a specific model ID like `gpt-4-32k` when invoking `llm` commands.

```Shell
llm -m 4-32k
```

--------------------------------

### Set default llm model via LLM_MODEL environment variable

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Configures the `LLM_MODEL` environment variable to change the default model for the current shell session. Subsequent `llm` commands will automatically use this specified model.

```bash
export LLM_MODEL=gpt-4.1-mini
llm 'Ten names for cheesecakes' # Uses gpt-4.1-mini
```

--------------------------------

### Embeddings Database SQL Schema

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/python-api.md

Provides the SQL schema for the `llm` project's embeddings database, detailing the `collections` and `embeddings` tables, their columns, data types, and relationships.

```sql
CREATE TABLE [collections] (
   [id] INTEGER PRIMARY KEY,
   [name] TEXT,
   [model] TEXT
)
CREATE TABLE "embeddings" (
   [collection_id] INTEGER REFERENCES [collections]([id]),
   [id] TEXT,
   [embedding] BLOB,
   [content] TEXT,
   [content_blob] BLOB,
   [content_hash] BLOB,
   [metadata] TEXT,
   [updated] INTEGER,
   PRIMARY KEY ([collection_id], [id])
)
```

--------------------------------

### Enable Error Raising and Debugging for LLM Prompts

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Set the `LLM_RAISE_ERRORS` environment variable to `1` to prevent error suppression during `llm prompt` execution. This allows for immediate error visibility and enables dropping into a Python debugger using `pdb.pm()` after running a prompt in interactive mode.

```Bash
export LLM_RAISE_ERRORS=1
```

```Python
python -i -m llm 'prompt'
import pdb; pdb.pm()
```

--------------------------------

### LLM Embedding Model Configuration API

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

API documentation for managing default embedding models within the `llm` library. These methods function analogously to their non-embedding counterparts for text generation models.

```APIDOC
llm.set_default_embedding_model(alias: str)
  alias: The model ID or alias to set as the default embedding model.
  Purpose: Sets the system-wide default embedding model. Persisted in configuration.

llm.get_default_embedding_model(default: Any = 'gpt-4o-mini') -> str | None
  default: (Optional) The value to return if no default embedding model is set. Defaults to 'gpt-4o-mini'.
  Purpose: Returns the currently configured default embedding model.
```

--------------------------------

### Embed a Single String with an Embedding Model

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/python-api.md

Shows how to embed a single string into a vector (list of floats) using the `.embed()` method of an `llm` embedding model.

```Python
vector = embedding_model.embed("my happy hound")
```

--------------------------------

### Check Recent LLM Logs

Source: https://github.com/simonw/llm/blob/main/docs/other-models.md

This command displays the most recent log entry from LLM, useful for confirming that prompts run against configured models were correctly processed and logged.

```bash
llm logs -n 1
```

--------------------------------

### Continue Specific Conversation by ID using llm

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Demonstrates how to continue a specific conversation that is not the most recent one using the '--cid' or '--conversation' option with a conversation ID. This allows users to pick up older conversations from the 'llm logs' command, providing flexibility in managing dialogue history.

```bash
llm 'More names' --cid 01h53zma5txeby33t1kbe3xk8q
```

--------------------------------

### Embed Multiple Items with Custom Batch Size

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/python-api.md

Explains how to specify a custom batch size for `embed_multi()` to control processing, especially useful for large datasets or memory management.

```Python
vectors = list(embedding_model.embed_multi(lines_from_file, batch_size=20))
```

--------------------------------

### Register LLM Embedding Model

Source: https://github.com/simonw/llm/blob/main/docs/plugins/plugin-hooks.md

This hook allows plugins to register additional embedding models. The provided code snippet shows how to define an `EmbeddingModel` that implements the `embed_batch` method to return fixed embedding vectors for a batch of items.

```Python
import llm

@llm.hookimpl
def register_embedding_models(register):
    register(HelloWorld())

class HelloWorld(llm.EmbeddingModel):
    model_id = "helloworld"

    def embed_batch(self, items):
        return [[1, 2, 3], [4, 5, 6]]
```

--------------------------------

### Decode binary embedding to NumPy array in Python

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/storage.md

Illustrates how to decode a little-endian binary embedding into a NumPy array using `np.frombuffer` with the `<f4` format string, ensuring correct interpretation of 32-bit floating-point data.

```Python
import numpy as np

numpy_array = np.frombuffer(value, "<f4")
```

--------------------------------

### View LLM Logs for Most Recent Conversation

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

This command specifically retrieves and displays all log entries associated with the most recent conversation you've had with an `llm` model.

```bash
llm logs -c
```

--------------------------------

### Set Default LLM Model

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Configure a specific model as the default for `llm` commands. When no model is explicitly specified with `-m` or `--model`, this default model will be used.

```Shell
llm models default MODEL_ID
```

--------------------------------

### Set Default Embedding Model for Collections

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Before storing embeddings in collections, it's recommended to set a default model using `llm embed-models default`. This ensures consistency and avoids repetitive model specification.

```bash
llm embed-models default 3-small
```

--------------------------------

### View LLM Logs for Specific Conversation ID

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

To view logs for a particular conversation, provide its unique ID using the `--cid` or `--conversation` flag. This allows precise retrieval of conversation history.

```bash
llm logs --cid 01h82n0q9crqtnzmf13gkyxawg
```

--------------------------------

### Output LLM Logs in JSON Format

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

This command changes the output format of the log messages to JSON, making it easier to parse programmatically. It's ideal for integration with other scripts or applications.

```bash
llm logs --json
```

--------------------------------

### Adding a prefix to embedded file IDs

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Shows how to use the `--prefix` option with `llm embed-multi` to add a custom prefix to the IDs generated for embedded files. This helps organize and categorize embeddings, especially when combining data from multiple sources.

```bash
llm embed-multi documentation \
  -m 3-small \
  --files docs '**/*.md' \
  -d documentation.db \
  --store \
  --prefix llm-docs/
```

--------------------------------

### Generate Structured JSON with Pydantic Schema

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

Learn how to use a Pydantic `BaseModel` to define the expected JSON schema for an LLM response. This ensures the model's output conforms to a predefined structure, making it easier to parse and use in Python applications.

```python
import llm, json
from pydantic import BaseModel

class Dog(BaseModel):
    name: str
    age: int

model = llm.get_model("gpt-4o-mini")
response = model.prompt("Describe a nice dog", schema=Dog)
dog = json.loads(response.text())
print(dog)
# {"name":"Buddy","age":3}
```

--------------------------------

### Retrieve Similar Items by Existing Item ID

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/python-api.md

Shows how to use the `collection.similar_by_id()` method to find items most similar to an existing item in the collection, identified by its ID. The item itself is excluded from the results.

```python
for entry in collection.similar_by_id("cat"):
    print(entry.id, entry.score)
```

--------------------------------

### LLM YAML Template with Embedded Python Functions

Source: https://github.com/simonw/llm/blob/main/docs/templates.md

Illustrates how to embed Python code defining custom `functions` directly within a YAML template using a multi-line string. These functions become available for the language model to call.

```yaml
name: my-functions
functions: |
  def reverse_string(s: str):
      return s[::-1]

  def greet(name: str):
      return f"Hello, {name}!"
```

--------------------------------

### Turn Off LLM Logging by Default

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

This command globally disables logging for all subsequent `llm` prompts and responses. Logging will remain off until explicitly re-enabled.

```bash
llm logs off
```

--------------------------------

### Bash: Recording Resolved Model Names with response.set_resolved_model()

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

When an `llm` plugin uses a model alias, `response.set_resolved_model()` can record the actual model ID executed. This ensures accurate logging of the specific model used, which is then visible in `llm logs` output and the database.

```bash
response.set_resolved_model(resolved_model_id)
```

--------------------------------

### YAML Configuration: Disable Model Streaming

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

This YAML configuration option allows custom OpenAI-compatible models to declare that they do not support streaming. Setting `can_stream` to `false` ensures that the system handles such models appropriately without attempting to stream responses.

```YAML
can_stream: false
```

--------------------------------

### Truncate LLM Log Output

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The `llm logs --truncate` (or `-t`) option allows users to shorten the displayed prompts in the log output, making it easier to review past interactions. This improves readability for lengthy prompts.

```Shell
llm logs --truncate
```

--------------------------------

### Retrieving Logged LLM Conversation Data

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

Shows how to retrieve the JSON data captured in the most recent `llm` conversation from the SQLite database. The `-c` flag specifies the most recent conversation, and `--data` outputs only the JSON response data.

```bash
llm logs -c --data
```

--------------------------------

### Opt-Out of LLM Response Streaming

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

LLM responses now stream by default if supported by the model, removing the need for the `-s/--stream` option. To disable streaming and receive the full response at once, use the new `--no-stream` option.

```Shell
llm --no-stream
```

--------------------------------

### Set Default Embedding Model via Environment Variable for llm embed

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Explains how to set the `LLM_EMBEDDING_MODEL` environment variable to define a default embedding model for all `llm embed` commands within the current shell session, simplifying command usage.

```bash
export LLM_EMBEDDING_MODEL=3-small
```

```bash
llm embed -c 'This is some content'
```

--------------------------------

### View Logged Items for a Specific Schema

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

This command retrieves logged JSON objects from `llm` runs. It filters logs by the 'people' schema (`--schema t:people`) and extracts the content of the 'items' array from each logged object, outputting them as newline-delimited JSON.

```bash
llm logs --schema t:people --data-key items
```

--------------------------------

### Bulk Embed into Collection with Custom Batch Size

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/python-api.md

Explains how to adjust the `batch_size` argument for `collection.embed_multi()` to manage memory usage when embedding large collections, especially with generators.

```Python
collection.embed_multi(
    (
        (i, line)
        for i, line in enumerate(lines_in_file)
    ),
    batch_size=10
)
```

--------------------------------

### Extract Newline-Delimited JSON Data from llm Logs

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

After generating schema-based JSON, this command shows how to retrieve the logged data. Using 'llm logs --schema-multi' with the '--data' option outputs the collected JSON data as newline-delimited JSON, allowing for easy processing of individual records.

```bash
llm logs --schema-multi 'name, ten_word_bio' --data
```

```json
{"items": [{"name": "Robo", "ten_word_bio": "A cybernetic dog with laser eyes and super intelligence."}, {"name": "Flamepaw", "ten_word_bio": "Fire-resistant dog with a talent for agility and tricks."}]}
{"items": [{"name": "Bolt", "ten_word_bio": "Lightning-fast border collie, loves frisbee and outdoor adventures."}, {"name": "Luna", "ten_word_bio": "Mystical husky with mesmerizing blue eyes, enjoys snow and play."}, {"name": "Ziggy", "ten_word_bio": "Quirky pug who loves belly rubs and quirky outfits."}]}
```

--------------------------------

### Clear Default LLM Model Options

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Commands to remove default options. 'llm models options clear <model_id> <option_name>' clears a specific option, and 'llm models options clear <model_id>' clears all default options for a given model.

```bash
llm models options clear gpt-4o temperature
```

```bash
llm models options clear gpt-4o
```

--------------------------------

### Debugging LLM Plugins: Enabling Error Raising with LLM_RAISE_ERRORS

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

To debug `llm` plugins, set the `LLM_RAISE_ERRORS` environment variable to `1` to force errors to be raised instead of logged. This allows Python's interactive mode (`-i`) to drop into a shell, where `pdb.pm()` can be used to enter a debugger at the point of the most recent error.

```bash
LLM_RAISE_ERRORS=1 python -i -m llm ...
```

```python
import pdb; pdb.pm()
```

--------------------------------

### Extract Most Recent LLM Response as Plain Text

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

Use this command to retrieve only the response from the most recent logged item, presented as plain text. This is useful for piping the response to other tools.

```bash
llm logs -r
```

--------------------------------

### Check if Collection Exists in Database

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/python-api.md

Demonstrates how to use the `Collection.exists` class method to determine if a collection with a specific name already exists within a given database instance.

```python
if Collection.exists(db, "entries"):
    print("The entries collection exists")
```

--------------------------------

### Filter LLM Logs by Model ID

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

Filter the `llm` command's logs to display entries for a specific model. This command accepts both model IDs and aliases.

```Shell
llm logs -m model_id
```

--------------------------------

### Set Default Embedding Model with `llm embed-models default`

Source: https://github.com/simonw/llm/blob/main/docs/help.md

The `llm embed-models default` subcommand allows users to view the currently set default embedding model or to specify a new one. It also provides an option to remove any previously set default model, reverting to no default.

```Shell
Usage: llm embed-models default [OPTIONS] [MODEL]

  Show or set the default embedding model

Options:
  --remove-default  Reset to specifying no default model
  -h, --help        Show this message and exit.
```

--------------------------------

### Python functions for encoding/decoding float arrays to binary

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/storage.md

Provides `encode` and `decode` Python functions using the `struct` module to convert between a list of floating-point numbers and a little-endian binary sequence (32-bit floats), suitable for efficient storage in SQLite BLOBs.

```Python
import struct

def encode(values):
    return struct.pack("<" + "f" * len(values), *values)

def decode(binary):
    return struct.unpack("<" + "f" * (len(binary) // 4), binary)
```

--------------------------------

### Define Supported Attachment Types for Multi-modal LLM Models

Source: https://github.com/simonw/llm/blob/main/docs/plugins/advanced-model-plugins.md

For multi-modal LLM models, specify the accepted attachment content types by defining the `attachment_types` class attribute as a set of MIME types. This allows LLM to validate attachments before passing them to the model's `execute()` method, ensuring only supported formats are processed.

```python
class NewModel(llm.Model):
    model_id = "new-model"
    attachment_types = {
        "image/png",
        "image/jpeg",
        "image/webp",
        "image/gif",
    }
```

--------------------------------

### Include IDs in Logged Schema Data Output

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

To track the origin of each data row, the '--data-ids' option can be added to include 'response_id' and 'conversation_id' fields in the output. These IDs correspond to the database entries for the response and conversation, providing valuable metadata for debugging or auditing.

```bash
llm logs --schema-multi 'name, ten_word_bio' --data-key items --data-ids
```

```json
{"name": "Nebula", "ten_word_bio": "A cosmic puppy with starry fur, loves adventures in space.", "response_id": "01jn4dawj8sq0c6t3emf4k5ryx", "conversation_id": "01jn4dawj8sq0c6t3emf4k5ryx"}
{"name": "Echo", "ten_word_bio": "A clever hound with extraordinary hearing, master of hide-and-seek.", "response_id": "01jn4dawj8sq0c6t3emf4k5ryx", "conversation_id": "01jn4dawj8sq0c6t3emf4k5ryx"}
{"name": "Biscuit", "ten_word_bio": "An adorable chef dog, bakes treats that everyone loves.", "response_id": "01jn4dawj8sq0c6t3emf4k5ryx", "conversation_id": "01jn4dawj8sq0c6t3emf4k5ryx"}
{"name": "Cosmo", "ten_word_bio": "Galactic explorer, loves adventures and chasing shooting stars.", "response_id": "01jn4daycb3svj0x7kvp7zrp4q", "conversation_id": "01jn4daycb3svj0x7kvp7zrp4q"}
{"name": "Pixel", "ten_word_bio": "Tech-savvy pup, builds gadgets and loves virtual playtime.", "response_id": "01jn4daycb3svj0x7kvp7zrp4q", "conversation_id": "01jn4daycb3svj0x7kvp7zrp4q"}
```

--------------------------------

### Python API for Setting and Removing Model Aliases

Source: https://github.com/simonw/llm/blob/main/docs/changelog.md

The LLM Python API provides functions to programmatically manage model aliases. `llm.set_alias` allows assigning a custom alias to a model ID, while `llm.remove_alias` can be used to delete an existing alias, offering flexible model management within Python code.

```APIDOC
llm.set_alias(alias: str, model_id: str)
llm.remove_alias(alias: str)
```

--------------------------------

### Set System-Wide Default LLM Model

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

The `llm.set_default_model()` function configures a system-wide default model, which can be a model ID or an alias. This setting is persisted in the LLM configuration folder and affects all programs using the `llm` library, including the CLI tool.

```Python
import llm

llm.set_default_model("claude-3.5-sonnet")
```

--------------------------------

### Clear Default Option(s) for an LLM Model

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Removes one or all default options set for a specific LLM model. This command is used to reset model configurations.

```Shell
Usage: llm models options clear [OPTIONS] MODEL [KEY]

  Clear default option(s) for a model

  Example usage:

      llm models options clear gpt-4o
      # Or for a single option
      llm models options clear gpt-4o temperature

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Collection Class API Reference

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/python-api.md

Defines the properties and methods available on a `Collection` instance for managing text embeddings, including ID, name, model, item count, embedding operations, similarity searches, and deletion. It also includes a class method to check for collection existence.

```APIDOC
Collection Class:
  Properties:
    id: integer ID of the collection in the database
    name: string name of the collection (unique in the database)
    model_id: string ID of the embedding model used for this collection
  Methods:
    model(): returns the EmbeddingModel instance, based on that model_id
    count(): returns the integer number of items in the collection
    embed(id: str, text: str, metadata: dict=None, store: bool=False): embeds the given string and stores it in the collection under the given ID. Optionally includes metadata (stored as JSON) and stores the text content itself.
    embed_multi(entries: Iterable, store: bool=False, batch_size: int=100): embeds multiple entries.
    embed_multi_with_metadata(entries: Iterable, store: bool=False, batch_size: int=100): embeds multiple entries with metadata.
    similar(query: str, number: int=10): returns a list of entries most similar to the embedding of the given query string.
    similar_by_id(id: str, number: int=10): returns a list of entries most similar to the embedding of the item with the given ID.
    similar_by_vector(vector: List[float], number: int=10, skip_id: str=None): returns a list of entries most similar to the given embedding vector, optionally skipping an entry.
    delete(): deletes the collection and its embeddings from the database
  Class Methods:
    Collection.exists(db, name): returns a boolean indicating if a collection exists in a database.
```

--------------------------------

### Disable Logging for a Single LLM Prompt

Source: https://github.com/simonw/llm/blob/main/docs/logging.md

Use this command to prevent a specific prompt and its corresponding response from being recorded in the `llm` log database. This is useful for sensitive or temporary queries.

```bash
llm 'Ten names for cheesecakes' -n
```

--------------------------------

### Extract Specific Nested JSON Data from llm Logs

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

When the logged JSON data contains nested structures, such as an 'items' key, the '--data-key' option can be used to directly access and output the content of that specific key. This simplifies parsing by extracting the desired list of objects directly.

```bash
llm logs --schema-multi 'name, ten_word_bio' --data-key items
```

```json
{"name": "Bolt", "ten_word_bio": "Lightning-fast border collie, loves frisbee and outdoor adventures."}
{"name": "Luna", "ten_word_bio": "Mystical husky with mesmerizing blue eyes, enjoys snow and play."}
{"name": "Ziggy", "ten_word_bio": "Quirky pug who loves belly rubs and quirky outfits."}
{"name": "Robo", "ten_word_bio": "A cybernetic dog with laser eyes and super intelligence."}
{"name": "Flamepaw", "ten_word_bio": "Fire-resistant dog with a talent for agility and tricks."}
```

--------------------------------

### Set Default Embedding Model with llm CLI

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

This command allows setting a specific embedding model as the default for `llm embed` and `llm embed-multi` commands. Any of the supported aliases for a model can be passed to this command, streamlining future embedding operations.

```bash
llm embed-models default 3-small
```

--------------------------------

### Define LLM Model Alias

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

The `llm.set_alias()` function allows defining a new alias for a model identifier or another existing alias. This change is persisted in the `aliases.json` file, which will be created or overwritten if invalid.

```Python
import llm

llm.set_alias("mini", "gpt-4o-mini")
```

--------------------------------

### Using an LLM Alias for Embedding a String (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/aliases.md

This command uses a defined alias (`oai`) to embed a given string. The `-c` flag provides the content to be embedded, and `-m` specifies the embedding model alias to be used.

```bash
llm embed -c 'hello world' -m oai
```

--------------------------------

### Filter LLM Logs by Specific Fragment ID

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

This command filters the `llm` logs to show only conversations that utilized a specific fragment. The `-f` or `--fragment` option accepts a fragment hash ID, URL, file path, or alias to narrow down the log results.

```bash
llm logs -c -f 0d6e368f9bc21f8db78c01e192ecf925841a957d8b991f5bf9f6239aa4d81815
```

--------------------------------

### Remove Fragment Alias using llm

Source: https://github.com/simonw/llm/blob/main/docs/usage.md

Illustrates the 'llm fragments remove' command, which removes an alias for a fragment. It clarifies that this command only removes the alias and does not delete the fragment record itself, as fragments are linked to previous prompts and responses and cannot be deleted independently.

```bash
llm fragments remove cli
```

--------------------------------

### Output Logged Schema Data as JSON Array

Source: https://github.com/simonw/llm/blob/main/docs/schemas.md

Instead of newline-delimited JSON, the '--data-array' option can be combined with other filters to output the extracted schema data as a single JSON array. This format is often preferred for direct consumption by applications or APIs that expect a complete array of objects.

```bash
llm logs --schema-multi 'name, ten_word_bio' --data-key items --data-array
```

```json
[{"name": "Bolt", "ten_word_bio": "Lightning-fast border collie, loves frisbee and outdoor adventures."},
 {"name": "Luna", "ten_word_bio": "Mystical husky with mesmerizing blue eyes, enjoys snow and play."},
 {"name": "Ziggy", "ten_word_bio": "Quirky pug who loves belly rubs and quirky outfits."},
 {"name": "Robo", "ten_word_bio": "A cybernetic dog with laser eyes and super intelligence."},
 {"name": "Flamepaw", "ten_word_bio": "Fire-resistant dog with a talent for agility and tricks."}]
```

--------------------------------

### Adding an Alias for an LLM Embedding Model (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/aliases.md

This command sets an alias specifically for an embedding model. The `oai` alias is created for the OpenAI `ada-002` embedding model, allowing for easier reference in embedding operations.

```bash
llm aliases set oai ada-002
```

--------------------------------

### Disable Prompt Logging (llm logs off)

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Deactivates logging for all future `llm` prompts and responses. This command stops the recording of interactions into the logs database, useful for privacy or performance.

```Shell
Usage: llm logs off [OPTIONS]

  Turn off logging for all prompts

Options:
  -h, --help  Show this message and exit.
```

--------------------------------

### Remove alias for an LLM fragment

Source: https://github.com/simonw/llm/blob/main/docs/fragments.md

Illustrates how to delete an existing alias for a fragment using the `llm fragments remove` command. This helps manage and clean up fragment aliases.

```bash
llm fragments remove mydocs
```

--------------------------------

### Delete Embedding Collection from Specific Database with llm CLI

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

To delete a collection from a non-default database file, use the `-d` option along with the database file path and the collection name. This ensures the correct collection is removed from the intended database.

```bash
llm collections delete collection-name -d my-embeddings.db
```

--------------------------------

### Unset Default Embedding Model with llm CLI

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

Use the `--remove-default` option to clear the currently set default embedding model. When no default is set, the `llm embed` and `llm embed-multi` commands will require that a model is explicitly specified using `-m/--model`.

```bash
llm embed-models default --remove-default
```

--------------------------------

### Removing an LLM Model Alias (Bash)

Source: https://github.com/simonw/llm/blob/main/docs/aliases.md

This command removes a specified model alias from the LLM configuration. It deactivates the `mini` alias, meaning `gpt-4o-mini` must be referred to by its full ID again if needed.

```bash
llm aliases remove mini
```

--------------------------------

### Remove LLM Model Alias

Source: https://github.com/simonw/llm/blob/main/docs/python-api.md

The `llm.remove_alias()` function removes a specified alias from the `aliases.json` configuration file. It raises a `KeyError` if the alias does not exist.

```Python
import llm

llm.remove_alias("turbo")
```

--------------------------------

### Delete an llm Collection

Source: https://github.com/simonw/llm/blob/main/docs/help.md

Deletes a specified `llm` collection from the embeddings database. This action requires the collection name as an argument and supports specifying a custom database path for the operation.

```Bash
Usage: llm collections delete [OPTIONS] COLLECTION

  Delete the specified collection

  Example usage:

      llm collections delete my-collection

Options:
  -d, --database FILE  Path to embeddings database
  -h, --help           Show this message and exit.
```

--------------------------------

### Delete an Embedding Collection with llm CLI

Source: https://github.com/simonw/llm/blob/main/docs/embeddings/cli.md

This command allows deleting a specified collection from the embeddings database. Provide the name of the collection to be removed to free up space or remove outdated data.

```bash
llm collections delete collection-name
```

=== COMPLETE CONTENT === This response contains all available snippets from this library. No additional content exists. Do not make further requests.