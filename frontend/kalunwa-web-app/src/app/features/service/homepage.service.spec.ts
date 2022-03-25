import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from "@angular/common/http/testing";
import { HomepageService } from './homepage.service';
import { EventsModel } from '../models/events';
import { JumbotronModel } from '../models/slides-model';

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

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/homepage/jumbotrons');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(testJumbotrons);

  });


});
