import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs';
import { IndivNewsModel } from 'src/app/features/models/indiv-news-model';
import { NewsService } from '../service/news.service';

@Component({
  selector: 'app-indiv-news',
  templateUrl: './indiv-news.component.html',
  styleUrls: ['./indiv-news.component.scss']
})
export class IndivNewsComponent implements OnInit {

  @Input() latestNewsList: string[];
  news$: Observable<IndivNewsModel>;
  constructor(private route: ActivatedRoute, private newsService: NewsService) { }

  ngOnInit(): void {

    const newsId = this.route.snapshot.paramMap.get("id");
    this.news$ = this.newsService.getNewsDetails(newsId);
    this.news$.subscribe(news=> console.log(news));
  }

}
