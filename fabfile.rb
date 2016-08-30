# encoding: utf-8
cheatsheet do
  title '快速开发命令备忘'               # Will be displayed by Dash in the docset list
  docset_file_name '快速开发命令备忘'    # Used for the filename of the docset
  keyword 'develop'             # Used as the initial search keyword (listed in Preferences > Docsets)
  # resources 'resources_dir'  # An optional resources folder which can contain images or anything else

  introduction 'My *awesome* cheat sheet'  # Optional, can contain Markdown or HTML

  # A cheat sheet must consist of categories
  category do
    id 'Windows'  # Must be unique and is used as title of the category

    entry do
      command 'fab uu [-R <roule>]'         # Optional
      command 'CMD+SHIFT+N'   # Multiple commands are supported
      name 'Create window'    # A short name, can contain Markdown or HTML
      notes 'Some notes'      # Optional longer explanation, can contain Markdown or HTML
    end
    entry do
      command 'CMD+W'
      name 'Close window'
    end
  end

  category do
    id 'Code'
    entry do
      name 'Code sample'
      notes <<-'END'
        ```bash
        sample = "You can include code snippets as well"
        ```
        Or anything else **Markdown** or HTML.
      END
    end
  end

  notes 'Some notes at the end of the cheat sheet'
end