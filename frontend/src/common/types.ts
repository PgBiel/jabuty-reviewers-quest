export interface Game {
  game_id: number;
  name: string;
  image: string;
  release_year: number;
  developer: string;
  publisher: string;
  genre: string;
}

export interface StarredGame extends Game {
  stars: number;
}

export interface Review {
  review_id: number;
  game_id: number;
  author_id: number;
  stars: number;
  body: string;
}
