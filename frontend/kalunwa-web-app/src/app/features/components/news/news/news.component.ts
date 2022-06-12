import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { filter, map, toArray } from 'rxjs/operators';
import { AnnoucementModel, NewsResponseModel } from 'src/app/features/models/news-model';
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
  announcement= {
    'created_at': new Date(),
    'title': '',
    'meta_description': '',
    'description': '',
    'id': 0
  } as AnnoucementModel;
  latestNews : string[];

  ngOnInit(): void {
    this.newsList$ = this.newsService.getNewsList();

    const announcementSub = this.newsService.getAnnoucement().subscribe(
      (res:any) => {
        this.announcement = res[0];
        announcementSub.unsubscribe();
      }
    )
    this.newsDisplay$ = this.newsList$;
  }

  getLatestNews(newsId: number){
    const newSub = this.newsList$.pipe(
      map(news =>
        news.filter(item => item.id != newsId))
    ).subscribe(news => {
      this.latestNews = news.map(item => item.title) as string[];
      newSub.unsubscribe();
    });
  }

}
