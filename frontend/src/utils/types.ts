export type User = {
  id: number;
  username: string;
  email: string;
};

export type Product = {
  id: number;
  name: string;
  description: string;
  price: number;
};

export type Order = {
  id: number;
  userId: number;
  productId: number;
  date: string;
  total: number;
};