
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        if self.posts:
            for post in self.posts:
                print(post)
                print('-' * 50)
        else:
            print("No posts available.")

    def list_posts_by_author(self, author):
        posts_by_author = [post for post in self.posts if post.author == author]
        if posts_by_author:
            for post in posts_by_author:
                print(post)
                print('-' * 50)
        else:
            print(f"No posts by author: {author}")

    def delete_post(self, title):
        self.posts = [post for post in self.posts if post.title != title]

    def edit_post(self, title, new_title=None, new_content=None):
        for post in self.posts:
            if post.title == title:
                if new_title:
                    post.title = new_title
                if new_content:
                    post.content = new_content
                print(f"Post '{title}' updated successfully.")
                return
        print(f"Post with title '{title}' not found.")

    def latest_posts(self, count=5):
        latest = self.posts[-count:]  # Fetch the latest 'count' posts
        for post in latest:
            print(post)
            print('-' * 50)



def menu():
    print("Welcome to the Blog System!")
    print("1. Add Post")
    print("2. List All Posts")
    print("3. List Posts by Author")
    print("4. Delete Post")
    print("5. Edit Post")
    print("6. Show Latest Posts")
    print("7. Exit")

def main():
    blog = Blog()
    
    while True:
        menu()
        choice = input("Choose an option (1-7): ")

        if choice == '1':
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("Post added successfully!")
        
        elif choice == '2':
            print("Listing all posts:")
            blog.list_all_posts()
        
        elif choice == '3':
            author = input("Enter author name to filter posts: ")
            print(f"Listing posts by {author}:")
            blog.list_posts_by_author(author)
        
        elif choice == '4':
            title = input("Enter title of post to delete: ")
            blog.delete_post(title)
            print("Post deleted successfully!")
        
        elif choice == '5':
            title = input("Enter title of post to edit: ")
            new_title = input("Enter new title (or press enter to skip): ")
            new_content = input("Enter new content (or press enter to skip): ")
            blog.edit_post(title, new_title, new_content)
        
        elif choice == '6':
            print("Latest posts:")
            blog.latest_posts()
        
        elif choice == '7':
            print("Exiting the system...")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
