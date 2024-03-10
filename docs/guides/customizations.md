The following settings will help you customize the `drf-blog-package` to suit your custom needs.

## **BLOG_BRIDGER_POST**
You can use this setting to define a custom model for blog posts in your project. The default model has the following fields:

- `post_title`
- `post_body`
- `author`
- `created_at`

To define your custom model, add this to your settings:

```python
BLOG_BRIDGER_POST = "yourApp.models.YourPostModel"
```

## **BLOG_BRIDGER_COMMENT**
This setting helps you define a custom model to handle comments under blog posts. The default model has the following fields:

<div class="annotate" markdown>
- `comment` (1)
- `comment_author`
- `post`
- `created_at`
</div>

1. The user's comment text.

To define your custom model, add this to your settings:

```python
BLOG_BRIDGER_COMMENT = "yourApp.models.YourCommentModel"
```