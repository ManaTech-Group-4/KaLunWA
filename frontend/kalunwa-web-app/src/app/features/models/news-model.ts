export interface NewsResponseModel{
  id: number;
  title: string;
  description: string;
  image: {
      id: number;
      image: string;
  },
  date: string;
}
