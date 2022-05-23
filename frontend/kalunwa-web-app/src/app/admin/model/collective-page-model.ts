export class CollectivePageModel {
  id: number;
  title: string;
  start_date: string;
  camp: string;
  status: string;
  checked: boolean;
}
export class ImageSnippet {
  constructor(
    public src: number,
    public file:File){}
}

