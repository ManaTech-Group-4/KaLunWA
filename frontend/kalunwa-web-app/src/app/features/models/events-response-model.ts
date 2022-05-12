export interface EventsResponseModel{
  id: number;
  title: string;
  description: string;
  image: {
      image: string;
  },
  start_date: string;
  end_date: string;
  camp: string;
  status: string;
}
