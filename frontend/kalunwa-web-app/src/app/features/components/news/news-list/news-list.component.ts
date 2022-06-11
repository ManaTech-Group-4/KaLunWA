import { ChangeDetectorRef, Component, Input, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { NewsResponseModel } from 'src/app/features/models/news-model';

@Component({
  selector: 'app-news-list',
  templateUrl: './news-list.component.html',
  styleUrls: ['./news-list.component.scss']
})
export class NewsListComponent implements OnInit {

  @Input() news = [] as NewsResponseModel[];


  constructor(private ref: ChangeDetectorRef) { }

  activePage:number = 1;
  currentPage = 0;
  lastPage = 4;

  detectIfChanges(){
    this.ref.detectChanges();
  }

  updateDisplay(newPage:number){
    console.log(newPage,this.activePage);
    this.currentPage += (5*(newPage-this.activePage));
    if(this.currentPage < 0)
      this.currentPage = 0;

    this.lastPage = this.currentPage + 5;
    if(this.lastPage > this.news.length)
      this.lastPage = this.news.length;

    this.ref.detectChanges();
    this.activePage = newPage;
  }

  ngOnInit(): void {
  }

}
