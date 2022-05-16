import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Observable, of } from 'rxjs';
import { map } from 'rxjs/operators';
import { IndivNewsModel } from 'src/app/features/models/indiv-news-model';
import { NewsService } from '../service/news.service';

@Component({
  selector: 'app-indiv-news',
  templateUrl: './indiv-news.component.html',
  styleUrls: ['./indiv-news.component.scss']
})
export class IndivNewsComponent implements OnInit, OnDestroy {

  latestNewsList: {id: number,title:string}[];
  news$: Observable<IndivNewsModel>;
  constructor(private route: ActivatedRoute, private newsService: NewsService) { }

  ngOnInit(): void {

    const newsId = this.route.snapshot.paramMap.get("id");
    this.news$ = this.newsService.getNewsDetails(newsId);
    this.news$.subscribe(news=> console.log(news));
    this.getLatestNews(newsId);
  }

  ngOnDestroy(){
  }

  getLatestNews(newsId:string | null){

    this.newsService.getLatestNews(newsId).subscribe(list =>{
      this.latestNewsList = list;
    });
  }


}
