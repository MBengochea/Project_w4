CREATE TABLE `Games`(
    `game_id` BIGINT UNSIGNED NOT NULL,
    `title` VARCHAR(255) NOT NULL,
    `url` VARCHAR(255) NOT NULL,
    `description` VARCHAR(255) NOT NULL,
    `total_plays` BIGINT NOT NULL,
    `amazon_price` FLOAT(53) NOT NULL,
    `wishlisted` BIGINT NOT NULL,
    `complexity` FLOAT(53) NOT NULL,
    `num_ratings` BIGINT NOT NULL,
    `avg_rating` FLOAT(53) NOT NULL,
    `player_id` BIGINT NOT NULL,
    `play_time_id` BIGINT NOT NULL,
    PRIMARY KEY(`game_id`)
);
CREATE TABLE `Players`(
    `player_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `min_player` BIGINT NOT NULL,
    `max_players` BIGINT NOT NULL,
    `minimum_age` BIGINT NOT NULL
);
CREATE TABLE `game_to_category`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `game_id` BIGINT NOT NULL,
    `category_id` BIGINT NOT NULL
);
CREATE TABLE `categories`(
    `category_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` BIGINT NOT NULL
);
CREATE TABLE `playtime`(
    `playtime_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `min_playtime` BIGINT NOT NULL,
    `max_playtime` BIGINT NOT NULL
);
ALTER TABLE
    `game_to_category` ADD CONSTRAINT `game_to_category_category_id_foreign` FOREIGN KEY(`category_id`) REFERENCES `categories`(`category_id`);
ALTER TABLE
    `Games` ADD CONSTRAINT `games_player_id_foreign` FOREIGN KEY(`player_id`) REFERENCES `Players`(`player_id`);
ALTER TABLE
    `Games` ADD CONSTRAINT `games_play_time_id_foreign` FOREIGN KEY(`play_time_id`) REFERENCES `playtime`(`playtime_id`);
ALTER TABLE
    `game_to_category` ADD CONSTRAINT `game_to_category_game_id_foreign` FOREIGN KEY(`game_id`) REFERENCES `Games`(`game_id`);