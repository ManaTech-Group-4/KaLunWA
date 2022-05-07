import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { filter, map, toArray } from 'rxjs/operators';
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
  latestNews : string[];

  ngOnInit(): void {
    this.newsList$ = this.newsService.getNewsList();

    this.newsDisplay$ = this.newsList$;
  }

  getLatestNews(newsId: number){
    this.newsList$.pipe(
      map(news =>
        news.filter(item => item.id != newsId))
    ).subscribe(news => {
      this.latestNews = news.map(item => item.title) as string[];
    });
    console.log(this.latestNews);
  }

}
