export interface EventsModel{
  container:number;
  event:{
    id: number;
    title: string;
    image: {id:number; image: string};
  };
  id:number;
  section_order:number;

}
