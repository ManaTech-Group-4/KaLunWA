import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from "@angular/common/http/testing";
import { HomepageService } from './homepage.service';
import { EventsModel } from '../models/events';
import { JumbotronModel } from '../models/slides-model';
import { HomeNewsModel } from '../models/home-news';
import { homepageInfo } from '../models/homepage-container-model';

describe('HomepageService', () => {
  let homepageService: HomepageService,
      httpTestingController: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [
        HomepageService
      ]
    });
    homepageService = TestBed.get(HomepageService);
    httpTestingController = TestBed.get(HttpTestingController);
  });

  afterEach(()=>{
    httpTestingController.verify();
  });


  it('should retrieve all jumbotrons', () => {
    const homepageTest: homepageInfo.HomepageContainer = {
        id: 1,
        name: "homepage",
        slug: "homepage",
        page_contained_jumbotrons: [
            {
                id: 1,
                container: 1,
                jumbotron: {
                    id: 1,
                    header_title: "Plant.",
                    subtitle: "Let's grow and foster together.",
                    image: {
                        id: 1,
                        image: "http://127.0.0.1:8000/media/images/content/carousel1.jpg"
                    },
                    created_at: new Date(),
                    updated_at: new Date()
                },
                section_order: 1
            }
        ],
        page_contained_projects: [
            {
                id: 1,
                container: 1,
                project: {
                    id: 1,
                    title: "Project 1",
                    image: {
                        id: 9,
                        image: "http://127.0.0.1:8000/media/images/content/project.jpg"
                    },
                    description: "description 1",
                    start_date: new Date(),
                    end_date: new Date(),
                    camp: "General",
                    created_at: new Date(),
                    updated_at: new Date(),
                    status: "Past"
                },
                section_order: 1
            }
        ],
        page_contained_events: [
            {
                id: 1,
                container: 1,
                event: {
                    id: 1,
                    title: "Event 1",
                    image: {
                        id: 7,
                        image: "http://127.0.0.1:8000/media/images/content/event.jpg"
                    },
                    description: "description 1",
                    start_date: new Date(),
                    end_date: new Date(),
                    camp: "General",
                    created_at: new Date(),
                    updated_at: new Date(),
                    status: "Past"
                },
                "section_order": 1
            }
        ]
    }
    homepageService.getHomepage().subscribe((homepageData)=>{
      expect(homepageTest).toBe(homepageData,'should check mocked data');
    });

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/page-containers/homepage/?expand=page_contained_jumbotrons.jumbotron.image,page_contained_events.event.image,page_contained_projects.project.image');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(homepageTest);

  });


  it('should retrieve all news', () => {
    const testNews: HomeNewsModel[] = [
      {
        id: 3,
        title: "News Headline 3",
        description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco",
        date: "March 25, 2022",
        image: {image: "http://127.0.0.1:8000/media/images/content/news3.jpg"}
    },
    {
        id: 2,
        title: "News Headline 2",
        description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco",
        date: "March 25, 2022",
        image: {image: "http://127.0.0.1:8000/media/images/content/news2.jpg"}
    },
    {
        id: 1,
        title: "News Headline 1",
        description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco",
        date: "March 25, 2022",
        image: {image: "http://127.0.0.1:8000/media/images/content/news1.jpg"}
    }];

    homepageService.getNews().subscribe((news)=>{
      expect(testNews).toBe(news,'should check mocked data');
    });

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/news/?expand=image&omit=created_at,updated_at,image.id&query_limit=3');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(testNews);

  });

});
