instructions =[
    'SET FOREIGN_KEY_CHECKS=0;',
    'DROP TABLE IF EXISTS todo;',
    'DROP TABLE IF EXISTS user;',
    'SET FOREIGN_KEY_CHECKS=1;',
    """
        CREATE TABLE user(
        id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(50) NOT NULL,
        PASSWORD VARCHAR(100) NOT NULL
        )

    """,
    """
        CREATE TABLE todo(
        id INT PRIMARY KEY AUTO_INCREMENT,
        created_by INT NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT current_timestamp,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL,
        FOREIGN KEY (created_by) REFERENCES user(id)
        );
    """,
    ]
