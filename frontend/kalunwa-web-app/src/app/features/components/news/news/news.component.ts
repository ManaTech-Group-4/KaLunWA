import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { NewsResponseModel } from 'src/app/features/models/news-model';
import { NewsService } from '../service/news.service';

@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrls: ['./news.component.scss']
})
export class NewsComponent implements OnInit {

  constructor(private newsService: NewsService) { }

  newsList$! : Observable<NewsResponseModel[]>;
  newsDisplay$! : Observable<NewsResponseModel[]>;

  ngOnInit(): void {
    this.newsList$ = this.newsService.getNewsList();

    this.newsDisplay$ = this.newsList$;
  }

}
