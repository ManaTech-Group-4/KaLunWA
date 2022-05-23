import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';
import { CollectivePageModel } from '../model/collective-page-model';

import { CollectivePagesService } from './collective-pages.service';

describe('CollectivePagesService', () => {

  let mockData: CollectivePageModel[]=[
    {
    "id": 1,
    "camp": "Suba",
    "start_date" : "May 9",
    "status": "Ongoing",
    "title": "The Long and Winding Road",
    "checked": true
    },
    {
    "id": 2,
    "camp": "Baybayon",
    "start_date" : "May 9",
    "status": "Past",
    "title": "Yesterday",
    "checked": true
    },
    {
    "id": 3,
    "camp": "Lasang",
    "start_date" : "Oct 10",
    "status": "Ongoing",
    "title": "From Me To You",
    "checked": true
    }
  ];

  let service: CollectivePagesService;
  let httpTestingController: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports:[HttpClientTestingModule]});
    service = TestBed.inject(CollectivePagesService);
    httpTestingController = TestBed.get(HttpTestingController);
  });

  afterEach(()=>{
    httpTestingController.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });


  it('retrieve data from getEventList', () => {

    service.getEventList().subscribe((member)=>{
      expect(mockData).toBe(member,'should check mocked data');
    });

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/events/?omit=image,updated_at,created_at,description,end_date');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(mockData);

  });
  it('retrieve data from getProjectList', () => {

    service.getProjectList().subscribe((member)=>{
      expect(mockData).toBe(member,'should check mocked data');
    });

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/projects/?omit=image,updated_at,created_at,description,end_date');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(mockData);

  });

  it('retrieve data from getNewsList', () => {

    service.getNewsList().subscribe((member)=>{
      expect(mockData).toBe(member,'should check mocked data');
    });

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/news/?omit=image,updated_at,created_at,description,end_date');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(mockData);

  });


  it('retrieve data from getAnnoucementList', () => {

    service.getAnnouncementList().subscribe((member)=>{
      expect(mockData).toBe(member,'should check mocked data');
    });

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/announcements/?updated_at,created_at,description,end_date');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(mockData);

  });
});
