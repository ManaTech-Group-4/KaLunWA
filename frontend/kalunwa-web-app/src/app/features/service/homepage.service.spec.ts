import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from "@angular/common/http/testing";
import { HomepageService } from './homepage.service';
import { EventsModel } from '../models/events';
import { JumbotronModel } from '../models/slides-model';
import { HomeNewsModel } from '../models/home-news';

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



  it('should retrieve all events', () => {
    const testEvents: EventsModel[] = [
        {id: 1, title:'Event 1', image: 'image/link/1'},
        {id: 2, title:'Event E', image: 'image/link/2'},
        {id: 3, title:'Event 2', image: 'image/link/3'}];

    homepageService.getEvents().subscribe((events)=>{
      expect(testEvents).toBe(events,'should check mocked data');
    });

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/homepage/events');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(testEvents);

  });



  it('should retrieve all projects', () => {
    const testProjects: EventsModel[] = [
        {id: 1, title:'Project 1', image: 'image/link/1'},
        {id: 2, title:'Project 2', image: 'image/link/2'},
        {id: 3, title:'Project 3', image: 'image/link/3'}];

    homepageService.getProjects().subscribe((projects)=>{
      expect(testProjects).toBe(projects,'should check mocked data');
    });

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/homepage/projects');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(testProjects);

  });

  it('should retrieve all jumbotrons', () => {
    const testJumbotrons: JumbotronModel[] = [
        {id: 1, header_title:'Jumbotron 1', image: 'image/link/1', short_description: 'sample body 1'},
        {id: 1, header_title:'Jumbotron 2', image: 'image/link/2', short_description: 'sample body 2'},
        {id: 1, header_title:'Jumbotron 3', image: 'image/link/3', short_description: 'sample body 3'},
        {id: 1, header_title:'Jumbotron 4', image: 'image/link/4', short_description: 'sample body 4'}];

    homepageService.getJumbotron().subscribe((jumbotrons)=>{
      expect(testJumbotrons).toBe(jumbotrons,'should check mocked data');
    });

<<<<<<< HEAD
    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/homepage/jumbotrons');
=======
    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/jumbotrons/?expand=image&omit=created_at,updated_at,image.id&query_limit=5');
>>>>>>> main

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(testJumbotrons);

  });


  it('should retrieve all news', () => {
    const testNews: HomeNewsModel[] = [
      {
        id: 3,
        title: "News Headline 3",
        description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco",
        date: "March 25, 2022",
        image: "http://127.0.0.1:8000/media/images/content/news3.jpg"
    },
    {
        id: 2,
        title: "News Headline 2",
        description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco",
        date: "March 25, 2022",
        image: "http://127.0.0.1:8000/media/images/content/news2.jpeg"
    },
    {
        id: 1,
        title: "News Headline 1",
        description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco",
        date: "March 25, 2022",
        image: "http://127.0.0.1:8000/media/images/content/news1.jpg"
    }];

    homepageService.getNews().subscribe((news)=>{
      expect(testNews).toBe(news,'should check mocked data');
    });

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/homepage/news');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(testNews);

  });

});
