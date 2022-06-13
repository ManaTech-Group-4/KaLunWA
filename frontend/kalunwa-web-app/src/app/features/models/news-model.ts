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
export interface AnnoucementModel{
  id: number;
  title: string;
  description: string;
  meta_description: string;
  created_at: Date;
}
