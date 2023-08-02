CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

INSERT INTO "Users" ("first_name", "last_name", "email", "bio", "username", "password", "profile_image_url", "created_on", "active")
VALUES
  ('Logan', 'Belew', 'Logan.doe@example.com', 'Hello, I am Logan.', 'LoganBelew1', '1', 'https://example.com/johndoe.jpg', '2023-07-31', True),
  ('Logan', 'Welch', 'Logan.Welch@example.com', 'Hi, I am Logan.', 'LoganWelch1', '1', 'https://example.com/janesmith.jpg', '2023-07-31', True),
  ('Katie', 'Zarbock', 'Katie.Zarbock@example.com', 'Hey, I am Mike.', 'KatieZarbock1', '1', 'https://example.com/mikejohnson.jpg', '2023-07-31', True),
  ('Randy', 'Hamm', 'Randy.Hamm@example.com', 'Greetings, I am Emily.', 'RandyHamm1', '1', 'https://example.com/emilybrown.jpg', '2023-07-31', True),
  ('Austin', 'Warrick', 'Austin.Warrick@example.com', 'Nice to meet you, I am Alex.', 'AustinWarrick1', '1', 'https://example.com/alexlee.jpg', '2023-07-31', True);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);

CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);


CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`category_id`) REFERENCES `Categories`(`id`)
);
DROP TABLE Posts



INSERT INTO "Posts" ("id", "user_id", "category_id", "title", "publication_date", "content", "approved")
VALUES (NUll, 1, 1, 'Lample Post', '2023-11-31', 'This is a sample post content.', 1);


CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);



CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);



CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);
-- Insert a reaction into the "PostReactions" table


CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);
-- Insert a reaction into the "PostReactions" table



CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);



CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);


CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
INSERT INTO "Subscriptions" ("id", "follower_id", "author_id", "created_on")
VALUES (1, 1, 2, '2023-07-31');


CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`category_id`) REFERENCES `Categories`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
INSERT INTO "Comments" ("id", "post_id", "author_id", "content")
VALUES (NULL, 1, 2, 'This is a sample comment.');
CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);
-- Insert a reaction into the "PostReactions" table

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);
-- Insert a reaction into the "PostReactions" table


CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

INSERT INTO "PostReactions" ("id", "user_id", "reaction_id", "post_id")
VALUES (NULL, 1, 2, 1);
INSERT INTO "Reactions" ("id", "label", "image_url")
VALUES (NULL, 'Thumbs Up', 'https://example.com/sample_post.jpg');

INSERT INTO "TAGS" ("id", "label")
VALUES (NULL, '#Swifty');
INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');

INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');
INSERT INTO Users ("first_name", "last_name", "email", "bio", "username", "password", "profile_image_url", "created_on", "active")
VALUES
  ('Logan', 'Belew', 'Logan.doe@example.com', 'Hello, I am Logan.', 'LoganBelew1', '1', 'https://example.com/johndoe.jpg', '2023-07-31', True),
  ('Logan', 'Welch', 'Logan.Welch@example.com', 'Hi, I am Logan.', 'LoganWelch1', '1', 'https://example.com/janesmith.jpg', '2023-07-31', True),
  ('Katie', 'Zarbock', 'Katie.Zarbock@example.com', 'Hey, I am Mike.', 'KatieZarbock1', '1', 'https://example.com/mikejohnson.jpg', '2023-07-31', True),
  ('Randy', 'Hamm', 'Randy.Hamm@example.com', 'Greetings, I am Emily.', 'RandyHamm1', '1', 'https://example.com/emilybrown.jpg', '2023-07-31', True),
  ('Austin', 'Warrick', 'Austin.Warrick@example.com', 'Nice to meet you, I am Alex.', 'AustinWarrick1', '1', 'https://example.com/alexlee.jpg', '2023-07-31', True);
INSERT INTO Subscriptions ("id", "follower_id", "author_id", "created_on")
VALUES (1, 1, 2, '2023-07-31');
INSERT INTO "Posts" ("id", "user_id", "category_id", "title", "publication_date", "image_url", "content", "approved")
VALUES (1, 1, 1, 'Sample Post', '2023-07-31', 'https://example.com/sample_post.jpg', 'This is a sample post content.', 1);
INSERT INTO "Comments" ("id", "post_id", "author_id", "content")
VALUES (NULL, 1, 2, 'This is a sample comment.');
INSERT INTO "Reactions" ("id", "label", "image_url")
VALUES (NULL, 'Thumbs Up', 'https://example.com/sample_post.jpg');
INSERT INTO "TAGS" ("id", "label")
VALUES (NULL, '#Swifty');
INSERT INTO PostReactions ("id", "user_id", "reaction_id", "post_id")
VALUES (NULL, 1, 2, 1);
INSERT INTO "PostTags" ("id", "post_id", "tag_id")
VALUES (NULL, 1, 1);
INSERT INTO Tags (`id`, `label`) VALUES (NULL, 'Philosophy');
INSERT INTO Tags (`id`, `label`) VALUES (NULL, 'Conspiracy');
INSERT INTO Tags (`id`, `label`) VALUES (NULL, 'Jimmy Carter Fan Fic');
INSERT INTO Tags (`id`, `label`) VALUES (NULL, 'Recipes');
